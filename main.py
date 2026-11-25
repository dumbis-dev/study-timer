import customtkinter

# customtkinter.set_appearance_mode("system")


class App(customtkinter.CTk):
    """Window for the app"""

    MAX_TIMERS = 10

    def __init__(self):
        super().__init__()

        self.title("Study Timer")
        self.minsize(360, 0)
        self.attributes(topmost=True)
        self.timer_frame = customtkinter.CTkFrame(
            self, width=0, height=0, fg_color="transparent"
        )
        self.timer_frame.pack()

        self.button = customtkinter.CTkButton(self, text="+", command=self.add_timer)
        self.button.pack()

        self.timer_count = 0

    def add_timer(self):

        if self.timer_count >= App.MAX_TIMERS:
            return

        row = TimerRow(self.timer_frame, 10)
        row.pack()
        self.timer_count += 1


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


app = App()
app.mainloop()
