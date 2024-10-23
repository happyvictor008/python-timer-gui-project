from tabnanny import check
from tkinter import *
import math

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
real_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(real_timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text = "Timer", font=(FONT_NAME, 24, "bold"), fg = GREEN, bg = YELLOW)
    check_mark.config(text = "", font=(FONT_NAME, 12, "bold"), fg = GREEN, bg = YELLOW)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    # comment the *60 for test only
    work_sec = WORK_MIN #* 60
    short_break_sec = SHORT_BREAK_MIN #* 60
    long_break_sec = LONG_BREAK_MIN #* 60
    global reps
    reps += 1
    if reps %2 == 1:
        timer_label.config(text = "Work", fg = RED)
        timer(work_sec)
    elif reps == 8:
        timer_label.config(text="Long Break", fg=GREEN)
        reps = 0
        timer(long_break_sec)

    else:
        timer_label.config(text="Short Break", fg=PINK)
        timer(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def timer(num):
    min = math.floor(num / 60)
    sec = num % 60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text = f"{min}:{sec}")
    if num > -1:
        global real_timer
        real_timer= window.after(1000, timer, num - 1)
    else:
        start_timer()
        if reps %2 == 1:
            check_mark.config(text = f"✓" * math.floor(reps/2))


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg = YELLOW)
#Setup canvas
canvas = Canvas(width=200, height=224, bg = YELLOW, highlightthickness= 0)
img = PhotoImage(file = "tomato.png")
canvas.create_image(100,112,image = img)
timer_text = canvas.create_text(100,130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column = 1,row = 1)

#Setup label

timer_label = Label(text = "Timer", font=(FONT_NAME, 24, "bold"), fg = GREEN, bg = YELLOW)
timer_label.grid(column = 1, row = 0)

check_mark = Label(text = "", font=(FONT_NAME, 12, "bold"), fg = GREEN, bg = YELLOW)
check_mark.grid(column = 1, row = 3)

# Setup buttons

start_button = Button(text = "Start", font=(FONT_NAME, 16, "bold"), command=start_timer)
start_button.grid(column = 0, row = 2)
reset_button = Button(text = "Reset", font=(FONT_NAME, 16, "bold"), command = reset_timer)
reset_button.grid(column = 2, row = 2)


window.mainloop()