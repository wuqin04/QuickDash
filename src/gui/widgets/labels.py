import customtkinter

# implement these as label first, and change with variables when needed in future
class CountdownLabel(customtkinter.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         text="COUNTDOWN: ",
                         font=("Segoe", 30),
                         **kwargs)

class TimerLabel(customtkinter.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         font=("Segoe", 30),
                         **kwargs)
        
class EventLabel(customtkinter.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         font=("Segoe", 30),
                         **kwargs)