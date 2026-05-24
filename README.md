# File Backup and Sync Utility

## 1. Introduction

This project is a Python-based File Backup and Sync Utility that simulates how file synchronization works between two folders.

It detects new or modified files in a source directory and automatically copies them to a backup directory, maintaining consistency between both locations.

The project is designed for learning file handling and object-oriented design.

---

## 2. Directory Structure
```
Files-backup-utility/
│
├── README.md
├── main.py
|
├── src/
│ ├── sync_engine.py
│ ├── file_handler.py
│ ├── sync_analyser.py
│ ├── logger.py
│ └── system_config.py
│
├── docs/
│ ├── class_diagram.jpg
│ ├── class_diagram.ufx
│ └── Lesson34_sdd-file.pdf

```
---
## 3. System Overview

The system compares a **source folder** with a **backup folder**.

When changes are detected:
- New files are copied
- Modified files are updated
- Folder structure is preserved

The system can be run manually via command line.

---

## 4. System Features

- Directory comparison between source and backup
- Automatic file copying and updating
- Maintains folder structure
- Manual or loop-based synchronization
- Logging of all operations
  
---

## 5. Learning Outcomes

This project demonstrates:
- Object-Oriented Programming (OOP)
- Design patterns (Singleton, adapter and command)
- File system manipulation in Python
- Modular software design

---

## 6. Future Improvements

- Add real-time folder watching
- Implement file deletion sync
- Add hashing for faster comparison
- Add GUI interface
- Improve logging with file output
---

## 7. Author

Created as a learning project 
