# 📂 Automatic File Sorter

This Python script automatically organizes files from a given directory into specific folders based on their file type (Excel, Image, PDF).  

Currently, it sorts:
- `.xlsx` → **excel files/**
- `.png` → **image files/**
- `.pdf` → **pdf files/**

---

## 📁 Project Structure

```
C:/Users/LENOVO/Downloads/Automatic File Sorter Testing/
│
├── excel files/
├── image files/
├── pdf files/
├── file_sorter.py   # The Python script
```

> The script will automatically create the `excel files`, `image files`, and `pdf files` folders if they do not already exist.

---

## ⚙️ How It Works

1. The script scans the directory:  
   ```
   C:/Users/LENOVO/Downloads/Automatic File Sorter Testing/
   ```

2. It checks for `.xlsx`, `.png`, and `.pdf` files.

3. Based on the extension:
   - Moves Excel files into `excel files/`
   - Moves Images into `image files/`
   - Moves PDFs into `pdf files/`

4. If a folder does not exist, it is created automatically.

---

## ▶️ Usage

1. Clone or copy the script into your project folder.  
2. Make sure Python is installed (>= 3.6).  
3. Run the script:

```bash
python file_sorter.py
```

---

## 📦 Requirements

This project uses only Python’s built-in libraries:
- `os`
- `shutil`

So, no external dependencies are required.

---

## ✨ Example

Before running:
```
Automatic File Sorter Testing/
│
├── report.xlsx
├── picture.png
├── document.pdf
```

After running:
```
Automatic File Sorter Testing/
│
├── excel files/
│   └── report.xlsx
├── image files/
│   └── picture.png
├── pdf files/
│   └── document.pdf
```

---

## 📝 Notes

- The script currently only supports `.xlsx`, `.png`, and `.pdf` files.  
- You can easily extend it by adding more conditions in the `if-elif` block for different file types.  
- The path is **hardcoded**; you can change it inside the script to point to any folder.  

---
