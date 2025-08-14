import customtkinter
from settings import set_default_theme, set_default_appearance_mode

# settings 
set_default_appearance_mode()
set_default_theme()

# all design goes here
# the background frame
class BackgroundFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, 
                         width=650,
                         height=370,
                         **kwargs)
        
class TabFrameFront(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         width=627,
                         height=30,
                         corner_radius=15,
                         fg_color="#3C096C",
                         **kwargs)

# setup the app
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("QuickDash")
        self.geometry("680x400")
        self.resizable(width=False, height=False)

        self.background_frame = BackgroundFrame(master=self)
        self.background_frame.place(x=15, y=15)

        self.tab_frame = TabFrame(master=self.background_frame)
        self.tab_frame.place(x=10, y=333)

# app start running here
app = App()
app.mainloop()
