import customtkinter
from styles import set_default_theme

set_default_theme()
app = customtkinter.CTk()

# setup the window
app.title("QuickDash")
app.geometry("680x400")

# app start running here
app.mainloop()
