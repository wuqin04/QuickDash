# QuickDash TODO (Milestone Format)

## Stage A — Python MVP

### 1. Basic Window
- [x] Create project folders (`gui/`, `backend/`, `assets/`)
- [x] Set up virtual environment & install GUI framework
- [ ] Run empty `main.py` with a blank window
- [x] Export icons/images from Figma to `assets/`
- [ ] Save fonts, colors, sizes to `styles.py`

### 2. Static UI Layout
- [ ] Build main layout (Upcoming Event, Event List, Add button)
- [ ] Add placeholder form for new events

### 3. Event System
- [ ] Create `Event` class
- [ ] Create `EventManager` (save/load to JSON)
- [ ] Connect buttons (Add/Edit/Delete)
- [ ] Refresh event list on changes
- [ ] Add basic input checks

### 4. Next Event & Alerts
- [ ] Show nearest upcoming event in UI
- [ ] Show in-app alert before event start

### 5. Background Mode
- [ ] Add minimize-to-tray option
- [ ] Keep alerts running in background

---

## Stage B — C++ Background & OS Integration

### 6. Shared Storage
- [ ] Switch storage to SQLite via storage adapter
- [ ] Migrate old JSON data to SQLite

### 7. Background Service
- [ ] Create C++ service to read events & show OS notifications
- [ ] Make service auto-start at boot
- [ ] Clicking a notification opens GUI
- [ ] (Optional) Add Python ↔ C++ communication

### 8. Packaging & Docs
- [ ] Package Python GUI (PyInstaller)
- [ ] Package C++ service installer
- [ ] Write install/uninstall guide
