import customtkinter


class TimerRow(customtkinter.CTkFrame):
    """Frame that holds timer."""

    def __init__(self, master, time_input):
        """Initializing the class attributes."""
        super().__init__(master)
        self.label = customtkinter.CTkLabel(
            self, text="", corner_radius=8, border_width=2
        )
        self.button = customtkinter.CTkButton(
            self, text="Start", command=self.start_pause
        )
        self.label.pack()
        self.button.pack()

        self.time_input = time_input
        self.remaining = self.time_input
        self.timer_id = None
        self.update_label()

    def start_pause(self):
        """Configuration for button behaviour."""
        text = self.button.cget("text")
        if text == "Start":
            self.button.configure(text="Pause")
            self.update_label()
            self.timer_id = self.after(1000, self.countdown)
        elif text == "Pause":
            self.button.configure(text="Start")
            self.after_cancel(self.timer_id)
        elif text == "Restart":
            self.remaining = self.time_input
            self.update_label()
            self.button.configure(text="Pause")
            self.timer_id = self.after(1000, self.countdown)

    def countdown(self):
        """Counts down ticks."""
        self.remaining -= 1
        self.update_label()

        if self.remaining == 0:
            self.button.configure(text="Restart")
            return

        self.timer_id = self.after(1000, self.countdown)

    def update_label(self):
        """Converts remaining to digital time and then displays it on a label"""
        minutes, seconds = divmod(self.remaining, 60)
        self.label.configure(text=f"{minutes:02d}:{seconds:02d}")


app = customtkinter.CTk()
app.geometry("350x150")
app.title("Study Timer")
app.attributes(topmost=True)

row1 = TimerRow(app, 10)
row1.pack()
row2 = TimerRow(app, 5)
row2.pack()

app.mainloop()
