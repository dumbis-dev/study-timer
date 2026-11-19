import customtkinter


def countdown():
    global remaining
    if remaining == 0:
        label.configure(text="00:00")
        return
    minutes, seconds = divmod(remaining, 60)
    label.configure(text=f"{minutes:02d}:{seconds:02d}")
    remaining -= 1
    app.after(1000, countdown)


# def say_hello():
#     print("hello")
#     app.after(2000, say_hello)

app = customtkinter.CTk()
app.geometry("350x150")
app.title("Study Timer")
app.attributes(topmost=True)
label = customtkinter.CTkLabel(app, text="Hello Timer", corner_radius=8, border_width=2)
label.pack()
remaining = 10
countdown()


app.mainloop()
