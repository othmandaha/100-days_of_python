from tkinter import *
import math
# from tkinter.ttk import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks = ''
reset_on = False

# ---------------------------- TIMER RESET ------------------------------- # 
def resetTimer():
    global reps
    global reset_on
    reps = 0
    reset_on = True
    canvas.itemconfig(timeText, text="25:00")
    checkMark.config(text='')
    titleLabel.config(text='Timer') 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
    global reps
    global reset_on
    reset_on = False
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countDown(long_break_sec)
        titleLabel.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        countDown(short_break_sec)
        titleLabel.config(text='Break', fg=PINK)
    else:
        countDown(work_sec)
        titleLabel.config(text='Work', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countDown(count):
    global marks
    global reset_on
    min = math.floor(count / 60)
    sec = count % 60

    if reset_on == True:
        return
    if sec < 10:
        sec = "0{}".format(sec)
    if min < 10:
        min = "0{}".format(min)
    canvas.itemconfig(timeText, text="{}:{}".format(min, sec))
    if count > 0:
        window.after(1000, countDown, count - 1)
    else:
        if reps % 2 != 0:
            marks += '✔'
            checkMark.config(text=marks)
        startTimer()
# ---------------------------- UI SETUP ------------------------------- #

#*Setting the window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#*Importing the image
tomatoImg = PhotoImage(file="Day28-Pomodoro_app/tomato.png")
#*Make a canvas (for putting elements on top of each other)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
#*Tomato image
canvas.create_image(100, 112, image=tomatoImg)


#* Counter text
timeText =canvas.create_text(100, 130, text="25:00", fill='white', font=(FONT_NAME, 35, "bold") )
canvas.grid(row=1, column=1)


#* Title label
titleLabel = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, 'bold'))
titleLabel.grid(row=0, column=1)


#* Checkmarks label
checkMark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
checkMark.grid(row=3, column=1)


#* style for the buttons
# style = Style()
# style.configure('W.TButton', font =
#                ('calibri', 10, 'bold', 'underline'),
#                 foreground = 'red')

#* start button
startButton = Button(text="Start", command=startTimer)
startButton.grid(row=2, column=0)


#* reseet button
resetButton = Button(text="Reset", command=resetTimer)
resetButton.grid(row=2, column=2)


#!Keeps the window open
window.mainloop()