import customtkinter

class EventButton(customtkinter.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         fg_color="#7B2CBF",
                         corner_radius=12,
                         width=560,
                         height=65,
                         font=("Segeo", 30),
                         hover="#9D4EDD",
                         **kwargs)