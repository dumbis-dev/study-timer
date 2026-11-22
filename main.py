import customtkinter


def countdown():
    global remaining
    global timer_id

    remaining -= 1
    update_label()

    if remaining == 0:
        start_btn.configure(text="Restart")
        return

    timer_id = app.after(1000, countdown)


def start_pause():
    global remaining
    global timer_id

    text = start_btn.cget("text")
    if text == "Start":
        start_btn.configure(text="Pause")
        update_label()
        timer_id = app.after(1000, countdown)
    elif text == "Pause":
        start_btn.configure(text="Start")
        app.after_cancel(timer_id)
    elif text == "Restart":
        remaining = time_input
        update_label()
        start_btn.configure(text="Pause")
        timer_id = app.after(1000, countdown)


def update_label():
    """Converts remaining to digital time and then displays it on a label"""
    minutes, seconds = divmod(remaining, 60)
    label.configure(text=f"{minutes:02d}:{seconds:02d}")


app = customtkinter.CTk()
app.geometry("350x150")
app.title("Study Timer")
app.attributes(topmost=True)

time_input = 10
remaining = time_input
timer_id = None

label = customtkinter.CTkLabel(app, text="00:00", corner_radius=8, border_width=2)
update_label()
label.pack()


start_btn = customtkinter.CTkButton(app, text="Start", command=start_pause)
start_btn.pack()

app.mainloop()
