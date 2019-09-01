import pyautogui
import time
from pynput.mouse import Listener

""" This scripts clicks forward surveys or courses that make you wait between pages for some seconds or till a video is 
finished
"""
idx, idy = 0, 0

def main():

    print("Please fulscreen or don't move that window. Click on the posiion where you want the mouse to keep clicking")
    print("Waiting for mouse click position")

    def on_click(x, y, button, pressed):
        print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
        global idx, idy
        idx, idy = x,y
        if not pressed:
            # Stop listener
            return False
    # Collect events until released
    with Listener(on_click=on_click) as listener:
        listener.join()


    print("Enter time to wait between next between clicks. Example 30 if 30 secs between pages: ")
    time_duration = int(input())

    print("Enter how many pages to skip. 20 more pages to complete the course: ")
    pages = int(input())

    for i in range(pages):
        pyautogui.click(x=round(idx), y=round(idy)) # this works better even when you are using the mouse
        print("page {} skipped".format(i+1))
        time.sleep(time_duration)



if __name__== "__main__":
    main()
