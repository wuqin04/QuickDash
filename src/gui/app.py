import customtkinter
from settings import APP_TITLE, APP_SIZE, set_default_appearance_mode, set_default_theme
from widgets.frames import *
from widgets.tabs import *
from widgets.labels import *
from widgets.events import *
from widgets.buttons import EventButton

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
        self.back_tab_frame = BackTabFrame(master=self.background_frame)
        self.back_tab_frame.place(x=10, y=333)

        self.front_tab_frame = FrontTabFrame(master=self.back_tab_frame)
        self.front_tab_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.countdown_frame = CountdownFrame(master=self.background_frame)
        self.countdown_frame.place(x=10, y=10)

        # switch the event frame to button widgets
        self.top_event_frame = EventFrame(master=self.background_frame, width=560, height=65)
        self.top_event_frame.place(relx=.5, rely=.32, anchor="center")

        self.sec_event_frame = EventFrame(master=self.background_frame, width=532, height=67.75)
        self.sec_event_frame.place(relx=.5, rely=.52, anchor="center")

        self.third_event_frame = EventFrame(master=self.background_frame, width=505.4, height=58.9)
        self.third_event_frame.place(relx=.5, rely=.715, anchor="center")

        # Tab part
        self.event_reminder_tab = EventReminderTab(master=self.background_frame)
        self.event_reminder_tab.place(x=20, y=324, anchor="w")
        self.event_reminder_tab.lower(belowThis=self.back_tab_frame)

        self.quick_note_tab = QuickNoteTab(master=self.background_frame)
        self.quick_note_tab.place(x=135, y=324, anchor="w")
        self.quick_note_tab.lower(belowThis=self.back_tab_frame)

        # Label here
        self.countdown_label = CountdownLabel(master=self.countdown_frame)
        self.countdown_label.place(relx=0.5, rely=0.5, anchor="center")

        self.timer_label = TimerLabel(master=self.background_frame, text="5 Mins 30 Sec", text_color="#C77DFF")
        self.timer_label.place(x=350, y=30)

        # self.top_event_timer = TimerLabel(master=self.top_event_frame, text="5 Mins 30 Sec")
        # self.top_event_timer.place(relx=.5, rely=.5, anchor="w")

        self.sec_event_label = EventLabel(master=self.sec_event_frame, text="Event #2")
        self.sec_event_label.place(relx=.25, rely=.5, anchor="e")

        # self.sec_event_timer = TimerLabel(master=self.sec_event_frame, text="10 Mins 30 Sec")
        # self.sec_event_timer.place(relx=.5, rely=.5, anchor="w")

        self.third_event_label = EventLabel(master=self.third_event_frame, text="Event #3")
        self.third_event_label.place(relx=.25, rely=.5, anchor="e")

        # self.third_event_timer = TimerLabel(master=self.third_event_frame, text="15 Mins 30 Sec")
        # self.third_event_timer.place(relx=.5, rely=.5, anchor="w")

        # button here
        self.top_event_button = EventButton(master=self.top_event_frame, text="Event #1")
        self.top_event_button.place(relx=.5, rely=.5, anchor="center")

# app start running here
app = App()
app.mainloop()
