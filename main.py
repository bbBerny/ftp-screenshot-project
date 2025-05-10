import cv2 as cv
import numpy as np
import pyautogui as pg
import pygetwindow as pw
from ftplib import FTP
from dotenv import load_dotenv
import os

def open_camera():
    if not camera.isOpened():
        print('Unable to open camera!')
    else:
        gen = number_generator()
        while True:
            success, frame = camera.read()
            if not success:
                print('Unable to read camera!')
                break
            else:
                cv.imshow(WINDOW_NAME, frame)
            key = cv.waitKey(1) & 0xFF
            if key == ord('q'):
                ftp.quit()
                break
            if key == ord('s'):
                index = next(gen)
                screenshot = take_screenshot(WINDOW_NAME)
                save_image(screenshot, index)
                upload_image(index)
            if key == ord('c'):
                check_list()
        camera.release()
        cv.destroyAllWindows()

def take_screenshot(window_name: str):
    window = pw.getWindowsWithTitle(window_name)[0]
    if window:
        window.activate()
        x, y = window.topleft
        width, height = window.width, window.height
        screenshot = cv.cvtColor(np.array(pg.screenshot(region=(x, y, width, height))), cv.COLOR_RGB2BGR)
        return screenshot
    
def save_image(screenshot: cv.Mat, i: int):
    cv.imwrite(f'screenshot_{i}.jpg', screenshot)    
    print('Image saved!')

def number_generator():
    i = 0
    while True:
        yield i
        i += 1

def upload_image(i: int):
    print(i)
    with open(f'screenshot_{i}.jpg', 'rb') as f:
        ftp.storbinary(f'STOR screenshot_{i}.jpg', f)
        print('Image succesfully uploaded')

def check_list():
    files = ftp.nlst()
    print(files)


if __name__ == '__main__':
    # Connect camera
    camera = cv.VideoCapture(1)
    WINDOW_NAME = 'Camera Feed'

    # Load credentials
    load_dotenv()

    SERVER_IP = os.getenv('SERVER_IP')
    FTP_PORT = os.getenv('FTP_PORT')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')

    if not all([SERVER_IP, FTP_PORT, USER, PASSWORD]):
        print('Missing one or more environment variables:')
        print(f'SERVER_IP: {SERVER_IP}')
        print(f'FTP_PORT: {FTP_PORT}')
        print(f'USER: {USER}')
        print(f'PASSWORD: {PASSWORD}')
        exit(1)

    ftp = FTP()
    FTP_PORT = int(FTP_PORT)
    ftp.connect(SERVER_IP, FTP_PORT)
    ftp.login(USER, PASSWORD)
    # Main loop
    open_camera()




