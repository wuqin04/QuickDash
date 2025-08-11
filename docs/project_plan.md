# QuickDash — Tech Stack & Features

## Core Features

- 📅 **Exam & Event Reminders** — quick creation of time-based alerts  
- 📝 **Quick Notes** — jot down ideas, todos, and important info instantly  
- ✅ **Task Tracking** — simple checklist with completion tracking  
- 🔔 **Custom Notifications** — configurable desktop pop-ups and sounds  
- 🚀 **Runs on Startup** — launches automatically when your PC boots  
- 🎯 **Hotkey Toggle** — bring the dashboard up instantly from anywhere  
- 📂 **All-in-One View** — notes, tasks, and reminders in one place  
- 💾 **Offline Storage** — works without internet  

## Tech Stack

- **Frontend / GUI:** Python (Tkinter) — dashboard interface, reminders, notes, and alerts  
- **Backend Logic:** Python — task management, JSON/SQLite data storage, filtering, and sorting  
- **Background Services:** C++ — global hotkey listener, auto-start on boot, lightweight tray service  
- **Data Storage:** JSON (lightweight, easy to edit) or SQLite (more structured)  
- **OS Integration:**  
  - Windows Registry or Startup folder (via C++) for auto-run  
  - Windows API (via C++) for hotkeys and system tray  
  - `plyer` or `win10toast` (Python) for notifications  