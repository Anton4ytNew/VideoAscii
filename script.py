import cv2
import curses
import time

def imageasascii(image, width=80, height=40):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    symbols = [':', ';', 'l', '\\', '/', '0', '1', '|', 'p', 'b', 'm', '@', 'u', 'o', 'O', 'i', ' ']
    ascii_str = ''
    for i in range(height):
        for j in range(width):
            pixel = gray_image[i, j]
            ascii_str += symbols[min(pixel // 25, len(symbols) - 1)]
        ascii_str += '\n'
    return ascii_str

def playvideo(video_path):
    stdscr = curses.initscr()
    curses.curs_set(0)
    height, width = stdscr.getmaxyx()
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break 
        frame_resized = cv2.resize(frame, (width - 2, height - 2))
        ascii_frame = imageasascii(frame_resized, width=width - 2, height=height - 2)
        stdscr.clear()
        stdscr.addstr(0, 0, ascii_frame)
        stdscr.refresh()
        time.sleep(1 / 39)

    cap.release()

playvideo('путь/к/видео/video.mp4')
