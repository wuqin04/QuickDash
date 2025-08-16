import customtkinter

class CountdownLabel(customtkinter.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         text="COUNTDOWN",
                         font=("Segoe", 30),
                         **kwargs)
        
class TimerLabel(customtkinter.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         text="15 Minutes 30 Seconds",
                         font=("Segoe", 30),
                         **kwargs)
        
class EventLabel(customtkinter.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         font=("Segoe", 30),
                         **kwargs)