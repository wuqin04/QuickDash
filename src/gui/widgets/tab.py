import customtkinter

class EventReminderTab(customtkinter.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, 
                         width=98,
                         height=32,
                         text="Event Reminder",
                         **kwargs)

class QuickNoteTab(customtkinter.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         width=98,
                         height=32,
                         text="Quick Note",
                         **kwargs)