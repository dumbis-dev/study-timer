import customtkinter


def countdown():
    global remaining
    global timer_id

    minutes, seconds = divmod(remaining, 60)
    if remaining == 0:
        label.configure(text=f"{minutes:02d}:{seconds:02d}")
        startBtn.configure(text="Restart")
        return
    label.configure(text=f"{minutes:02d}:{seconds:02d}")
    remaining -= 1
    timer_id = app.after(1000, countdown)


def start_pause():
    global remaining

    text = startBtn.cget("text")
    if text == "Start":
        startBtn.configure(text="Pause")
        countdown()
    elif text == "Pause":
        startBtn.configure(text="Start")
        app.after_cancel(timer_id)
    elif text == "Restart":
        remaining = time_input
        startBtn.configure(text="Pause")
        countdown()


app = customtkinter.CTk()
app.geometry("350x150")
app.title("Study Timer")
app.attributes(topmost=True)
label = customtkinter.CTkLabel(app, text="Hello Timer", corner_radius=8, border_width=2)
label.pack()
time_input = 10
remaining = time_input
timer_id = None

startBtn = customtkinter.CTkButton(app, text="Start", command=start_pause)
startBtn.pack()

app.mainloop()
