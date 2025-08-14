import customtkinter

class BackgroundFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, 
                         width=650,
                         height=370,
                         **kwargs)
        
class TabFrameBack(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         width=627,
                         height=30,
                         corner_radius=15,
                         fg_color="#3C096C",
                         **kwargs)
        
class TabFrameFront(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         width=600,
                         height=5,
                         corner_radius=15,
                         fg_color="#5A189A",
                         **kwargs)