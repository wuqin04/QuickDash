# QuickDash TODO (Milestone Format)

## Stage A — Python MVP

### 1. Basic Window
- [x] Create project folders (`gui/`, `backend/`, `assets/`)
- [x] Set up virtual environment & install GUI framework
- [x] Run empty `main.py` with a blank window
- [x] Export icons/images from Figma to `assets/`
- [x] Save fonts, colors, sizes to `src/assets/themes/default.json` from customTkinter doc
- [x] Import the theme from `default.json` to `settings.py`
- [x] Customize own theme in `default.json`

### 2. Static UI Layout
- [x] Basic UI layout based on the image at `src/assets/images/QuickDash Dashboard Preview`
- [] Make Event List a clickable Frame
- [] Build main layout (Upcoming Event, Event List, Add Event)
- [] Add placeholder form for new events

### 3. Event System
- [] Create `Event` class
- [] Create `EventManager` (save/load to JSON)
- [] Connect buttons (Add/Edit/Delete)
- [] Refresh event list on changes
- [] Add basic input checks

### 4. Next Event & Alerts
- [] Show nearest upcoming event in UI
- [] Show in-app alert before event start

### 5. Background Mode
- [] Add minimize-to-tray option
- [] Keep alerts running in background

---

## Stage B — C++ Background & OS Integration

### 6. OS-Level Styling
- [] Prepare Python HWND retrieval for CTk window
- [] Create C++ DLL to remove default window border and apply rounded corners
- [] Integrate DLL with Python via `ctypes`
- [] Test styling on Windows, add fallback for other platforms
- [] Finalize and polish OS-level appearance

### 7. Shared Storage
- [] Switch storage to SQLite via storage adapter
- [] Migrate old JSON data to SQLite

### 8. Background Service
- [] Create C++ service to read events & show OS notifications
- [] Make service auto-start at boot
- [] Clicking a notification opens GUI
- [] (Optional) Add Python ↔ C++ communication

### 9. Packaging & Docs
- [] Package Python GUI (PyInstaller)
- [] Package C++ service installer
- [] Write install/uninstall guide
