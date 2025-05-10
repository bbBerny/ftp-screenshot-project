# FTP Screenshot Project

A python project that captures window screenshots and uploads them via File Transfer Protocol to a remote FTP server

## Requirements
- Python 3.7+
- Access to an FTP server
- A working webcam

## Setup

1. Install dependencies with `pip install -r requirements.txt` on the working directory

2. Create a `.env` file (you can copy `.env.example`) and fill in your FTP server details

> [!NOTE]
> As of now SFTP is not supported, FTP connection uses plain FTP, so credentials are not encrypted. 



## Usage

- Press `s` to take a screenshot, it will automatically save it in your working directory and also upload it to the server
- Press `q` to exit the camera feed

## Notes
- Screenshots are saved as `screenshot_<number>.jpg`
- As of now each time the code is ran, the images are overwritten, this will be fixed in the future
- Make sure the server is running and reachable
- Never upload your actual `.env` file or sensitive credentials to GitHub.


## Camera configuration

This project uses OpenCV to access your webcam. By default it uses `camera = cv.VideoCapture(1)`
If the program does not show your camera feed or prints `Unable to open camera!`, try changing the camera index to `0`
- `camera = cv.VideoCapture(0)`
- The number refers to the device index:
    - `0` is usually the built-in camera
    - `1`, `2`, etc. are external webcams
- You can test available indexes by incrementing the number and checking which one shows your desired feed