import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import imutils
import time

stream = cv2.VideoCapture("test2.mp4")
def play(speed):
    print("You clicked play. Speed is" ,speed)
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1 + speed)

    grabbed , frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width = 650, height = 500)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,anchor=tkinter.NW, image=frame)


def pending(decision):
    # 1. DISPLAY DECISION PENDING IMAGE
    frame = cv2.cvtColor(cv2.imread("dp.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=650, height = 353)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,anchor=tkinter.NW, image=frame)

    #2. WAIT FOR 1 second
    time.sleep(1)

    #3. DISPLAY SPONSER IMAGE
    frame = cv2.cvtColor(cv2.imread("sp.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=650, height = 353)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,anchor=tkinter.NW, image=frame)

    #4. WAIT FOR 1.5 seconds
    time.sleep(1.5)

    #5. DISPLAY OUT/NOT OUT
    if  decision=="out":
        decisionImg = "out1.jpg"
    else:
        decisionImg = "not.jpg"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=650, height = 353)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,anchor=tkinter.NW, image=frame)


def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is Out")

def not_out():
    thread = threading.Thread(target=pending, args=("notout",))
    thread.daemon = 1
    thread.start()
    print("Player is Not Out")

SET_WIDTH = 700
SET_HEIGHT = 500


#GUI STARTS HERE
window = tkinter.Tk()
window.title("DECISION REVIEW SYSTEM")
cv_img = cv2.cvtColor(cv2.imread("welcome.jpg"),cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window,width = 650, height = 490)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0,ancho=tkinter.NW, image=photo)
canvas.pack()


#BUTTONS TO CONTROL PLAYBACK

btn = tkinter.Button(window, text="<< Previous (fast)", width =50, command=partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="<< Previous (slow)", width =50, command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text="Next (fast) >>", width =50, command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text="Next (slow) >>", width =50, command=partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text="Give Out", width =50, command = out) 
btn.pack()

btn = tkinter.Button(window, text="Give Not Out", width =50, command = not_out)
btn.pack()


window.mainloop()