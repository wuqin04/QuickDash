import customtkinter
from widgets.events import event_button

class Button(customtkinter.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         command=event_button,
                         fg_color="#7B2CBF",
                         hover_color="#9D4EDD",
                         corner_radius=12,
                         border_width=0,
                         **kwargs)