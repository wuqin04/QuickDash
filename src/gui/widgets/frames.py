import customtkinter

class BackgroundFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, 
                         width=650,
                         height=370,
                         **kwargs)
        
class BackTabFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         width=627,
                         height=30,
                         corner_radius=15,
                         fg_color="#3C096C",
                         **kwargs)
        
class FrontTabFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         width=600,
                         height=5,
                         corner_radius=15,
                         fg_color="#5A189A",
                         **kwargs)
        
class CountdownFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         width=228,
                         height=69,
                         corner_radius=12,
                         fg_color="#3C096C",
                         **kwargs
                         )

# define your width and height when initialize this class
class EventFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         corner_radius=12,
                         border_width=0,
                         fg_color="#7B2CBF",
                         **kwargs)