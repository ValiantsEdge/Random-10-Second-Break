import random
from tkinter import *
import time
import datetime

breakCounter = 0
startTime = datetime.datetime.now()

def randomTime():
    randomTimeInt = random.randint(90, 240)
    # randomTimeInt = random.randint(1, 2)
    # Wait for length = randomTimeInt (1.5-4 minutes)
    countdown(randomTimeInt)
    print("Slept for " + str(randomTimeInt) + " seconds")
    # Make label show break prompt text
    text.config(text="Time for a 10 second break", fg = "Red", font = ("None", 16, "bold"))
    switchAck("Enable")
    # Bring Tkinter window to front of screen upon breaktime
    bringToFront(root)

def countdown(seconds):
    while seconds > 0:
        time.sleep(1)
        seconds -= 1
        print("Seconds remaining: " + str(seconds))            

def changeText(whichButton, stopTime = None):
    global breakCounter
    defaultText(text)
    if whichButton == "Ack":
        text.config(text="Started 10 second break")
        switchAck("Break")
        countdown(10)
        breakCounter += 1
        text.config(text="10 second break over")
        ackButton.config(bg="SeaGreen1")
        stopButton.config(state=NORMAL, bg = "Red")
        root.update()
    if whichButton == "Stop":
        breakText = "You took " + str(breakCounter) + " breaks"
        timeDifference = stopTime - startTime
        timeDifferenceMins = divmod(timeDifference.seconds, 60)
        if timeDifferenceMins[0] < 60:
            totalTimeMinsSec = "Your session lasted "+ str(timeDifferenceMins[0])+ " minutes and "+ str(timeDifferenceMins[1])+ " seconds \n" + breakText
            text.config(text=totalTimeMinsSec)
        else:
            timeDifferenceHours = divmod(timeDifferenceMins, 60)
            totalTimeHourMin = "Your session lasted "+ str(timeDifferenceHours[0])+ " hours and ", str(timeDifferenceHours[1])+ " minutes \n" + breakText
            text.config(text=totalTimeHourMin)

# Function for bringing Tkinter window to front of screen
def bringToFront(root):
    root.attributes("-topmost", True)
    root.attributes("-topmost", False)

# Root window 
root = Tk()
root.title("Randomly Spaced 10 Seconds")
root.config(pady=7, padx=7)

# Return text to defaults function
def defaultText(text):
    text.config(height=3, fg="Black", font=("None", 16))
    return text
text = Label(root, text="Press Start to begin session")
defaultText(text)
text.grid(row=0, column=0, columnspan=3)

# Function for disabling ack button
def switchAck(arg):
    if arg == "Enable":
        ackButton.config(state=NORMAL, bg="forest green")
        ackButton.update()
    if arg == "Disable":
        ackButton.config(state=DISABLED, bg="gray37")
        ackButton.update()
    if arg == "Break":
        ackButton.config(bg="blue violet")
        stopButton.config(state=DISABLED, bg="gray37")
        root.update()

# Start button
def startFunc():
    global startTime
    print("Start was clicked")
    startTime = datetime.datetime.now()
    text.config(text="Session Started")
    startButton.config(state=DISABLED, bg = "SeaGreen1")
    root.update()
    randomTime()
    startButton.config(bg="gray37")

startButton = Button(root, text="Start", 
                     command=startFunc,
                     height = 3,
                     width=20,
                     bd = 3,
                     bg = "forest green",
                     disabledforeground="Black",
                     )
startButton.grid(row=1,column=0)

# Stop button
def stopFunc():
    print("stop was clicked")
    stopTime = datetime.datetime.now()
    changeText("Stop",stopTime)
    startButton.config(state=NORMAL, bg="forest green")
    switchAck("Disable")

stopButton = Button(root, text="Stop",
                    command=stopFunc,
                    height=3,
                    width=20,
                    bd = 3,
                    bg = "red2",
                    disabledforeground="Black")
stopButton.grid(row=1,column=2)

# Acknowledge button
def ackFunc():
    print("ack was clicked")
    changeText("Ack")
    randomTime()

ackButton = Button(root, text="Acknowledge",
                   command=ackFunc,
                   height = 3,
                   width=20,
                   bd = 3,
                   disabledforeground="Black")
switchAck("Disable")
ackButton.grid(row=2, column=1)

root.mainloop()