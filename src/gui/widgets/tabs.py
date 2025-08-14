import customtkinter
from widgets.events import switch_tab

class EventReminderTab(customtkinter.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, 
                         width=98,
                         height=32,
                         text="Event Reminder",
                         command=switch_tab,
                         **kwargs)

class QuickNoteTab(customtkinter.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         width=98,
                         height=32,
                         text="Quick Note",
                         command=switch_tab,
                         **kwargs)