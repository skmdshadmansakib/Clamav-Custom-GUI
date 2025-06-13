# ClamAV Custom GUI Scanner

A Python-based graphical interface to run ClamAV antivirus scans on Windows.

---

## ✨ Features

- 📁 **Scan File or Folder** with two easy buttons:
  - `Select File to Scan`
  - `Select Folder to Scan`
- ✅ **Customizable Scan Options** via checkboxes:
  - `Run freshclam before scan (update database)`
  - `Recursive scan`
  - `Scan archives (e.g., zip, rar)`
  - `Enable heuristic scan`
  - `Minimum file size to scan (in KB)` — enter `0` for no limit
- 🧹 **Clear Logs** button to reset output display
- 📊 **Real-time ClamAV RAM Usage Monitor**
- 📄 **Big output window** showing live scan results
- 💾 Option to **save scan result as a .txt file**

---

## 🖥️ GUI Layout Preview

### 🖼️ Scan Result Interface

![GUI Result](https://github.com/skmdshadmansakib/Clamav-Custom-GUI/blob/main/Screenshot%202025-06-13%20111525.png?raw=true)

---

### 📄 Saved Scan Output File Example

![Text File Result](https://github.com/skmdshadmansakib/Clamav-Custom-GUI/blob/main/Screenshot%202025-06-13%20111609.png?raw=true)

---

## 🔧 How to Use

1. Make sure `clamscan.exe` and `freshclam.exe` are installed and configured.
2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
3. python clamav_gui.py

<h3 align="center">👨‍💻 Author</h3>
<p align="center"><b><a href="https://github.com/skmdshadmansakib">SK MD Shadman Sakib</a></b></p>
