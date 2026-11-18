import customtkinter

app = customtkinter.CTk()
app.geometry("350x150")
app.title("Study Timer")
app.attributes(topmost=True)
label = customtkinter.CTkLabel(app, text="Hello Timer", corner_radius=8, border_width=2)
label.pack()

app.mainloop()
