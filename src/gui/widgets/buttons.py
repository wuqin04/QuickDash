import customtkinter
from widgets.events import Event

event = Event()

class EventButton(customtkinter.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         fg_color="#7B2CBF",
                         corner_radius=12,
                         font=("Segeo", 25),
                         hover_color="#9D4EDD",
                         command=event.on_clicked,
                         **kwargs)