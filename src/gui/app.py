import customtkinter
from settings import APP_TITLE, APP_SIZE, set_default_appearance_mode, set_default_theme
from widgets.frame import BackgroundFrame, TabFrameBack, TabFrameFront
from widgets.tab import EventReminderTab, QuickNoteTab

# settings 
set_default_appearance_mode()
set_default_theme()

# setup the app
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title(APP_TITLE)
        self.geometry(APP_SIZE)
        self.resizable(width=False, height=False)

        # Background part
        self.background_frame = BackgroundFrame(master=self)
        self.background_frame.place(x=15, y=15)

        # Frame part
        self.tab_frame_back = TabFrameBack(master=self.background_frame)
        self.tab_frame_back.place(x=10, y=333)

        self.tab_frame_front = TabFrameFront(master=self.tab_frame_back)
        self.tab_frame_front.place(relx=0.5, rely=0.5, anchor="center")

        # Tab part
        self.event_reminder_tab = EventReminderTab(master=self.background_frame)
        self.event_reminder_tab.place(x=20, y=321)
        self.event_reminder_tab.lower(belowThis=self.tab_frame_back)

        self.quick_note_tav = QuickNoteTab(master=self.background_frame)
        self.quick_note_tav.place(x=135, y=321)
        self.quick_note_tav.lower(belowThis=self.tab_frame_back)

# app start running here
app = App()
app.mainloop()
