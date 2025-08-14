import customtkinter

class EventReminderTab(customtkinter.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, 
                         width=96,
                         height=32,
                         text="Event Reminder",
                         **kwargs)

