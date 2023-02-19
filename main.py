import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
check = "✓"
clock_timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    window.after_cancel(clock_timer)
    canvas.itemconfig(timer_text, text="00:00")
    main_label.config(text="TIMER", fg=GREEN)
    checkmark.config(text="")
    global reps
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps

    if reps % 8 == 0 and reps != 0:
        main_label.config(text="BREAK", fg=RED)
        timer = LONG_BREAK_MIN * 60


    else:
        if reps % 2 != 0:
            main_label.config(text="WORK", fg=GREEN)
            timer = WORK_MIN * 60

        else:
            main_label.config(text="BREAK", fg=PINK)
            timer = SHORT_BREAK_MIN * 60

    count_down(timer)
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global check
    global clock_timer

    minute_count = count // 60
    sec_count = count % 60
    if sec_count < 10:
        sec_count = "%02.0f" % sec_count
        # print(sec_count)

    canvas.itemconfig(timer_text, text=f"{minute_count}:{sec_count}")
    if count > 0:
        clock_timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 0:
            checkmark.config(text=f"{check}")
            check += "✓"
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# main heading
main_label = tkinter.Label(window, text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 42, "bold"))
main_label.grid(row=0, column=1)

# Tomato Image
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=tomato_img)
timer_text = canvas.create_text(101, 130, text="00:00", fill="white", font=(FONT_NAME, 45))
# canvas.create_text(101, 10, text="Timer", fill=GREEN, font=(FONT_NAME, 45, "bold"))
# canvas.config(padx=50, pady=39)
canvas.grid(row=1, column=1)

# Checkmarks
checkmark = tkinter.Label(window, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25))
checkmark.grid(row=3, column=1)

# Buttons
start_button = tkinter.Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", command=timer_reset)
reset_button.grid(row=2, column=2)

window.mainloop()
