import customtkinter
from settings import set_default_appearance_mode, set_default_theme
from widgets.frame import BackgroundFrame, TabFrameBack

# settings 
set_default_appearance_mode()
set_default_theme()

# setup the app
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("QuickDash")
        self.geometry("680x400")
        self.resizable(width=False, height=False)

        self.background_frame = BackgroundFrame(master=self)
        self.background_frame.place(x=15, y=15)

        self.tab_frame = TabFrameBack(master=self.background_frame)
        self.tab_frame.place(x=10, y=333)

# app start running here
app = App()
app.mainloop()
