import customtkinter

class countdownLabel(customtkinter.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         text="COUNTDOWN",
                         font=("Segoe UI", 30),
                         **kwargs)
        
class timerLabel(customtkinter.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         text="15 Minutes 30 Seconds",
                         font=("Segoe", 30),
                         **kwargs)