import random
from tkinter import *
import time
import datetime

breakCounter = 0
startTime = datetime.datetime.now()

def randomTime():
    # randomTimeInt = random.randint(90, 450)
    randomTimeInt = random.randint(1, 2)
    # Wait for length = randomTimeInt
    time.sleep(randomTimeInt)
    print("Slept for " + str(randomTimeInt) + " seconds")
    # Make label show break prompt text
    text.config(text="Time for a 10 second break")
    text.update()

def changeText(whichButton, stopTime = None):
    global breakCounter
    if whichButton == "Ack":
        text.config(text="Started 10 second break")
        text.update()
        breakCounter += 1
        time.sleep(5)
        text.config(text="10 second break over")
        text.update()
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
    
# Root window 
root = Tk()
root.title("Randomly Spaced 10 Seconds")
root.minsize(300,300)
root.maxsize(600,600)
root.geometry("300x300+50+50")

# Label
text = Label(root, text="")
text.pack()

# Start button
def startFunc():
    startTime = datetime.datetime.now()
    randomTime()
    
startButton = Button(root, text="Start", command=startFunc)
startButton.pack()

# Stop button
def stopFunc():
    stopTime = datetime.datetime.now()
    changeText("Stop",stopTime)

stopButton = Button(root, text="Stop", command=stopFunc)
stopButton.pack()

# Acknowledge button
def ackFunc():
    changeText("Ack")
    randomTime()

ackButton = Button(root, text="Acknowledge", command=ackFunc)
ackButton.pack()

root.mainloop()