# 📁 CloneX

A simple, beginner-friendly Python script that scans a folder and identifies duplicate files using SHA256 hashing.

## 🎯 What Does CloneX Do?

This script helps you:
- **Find duplicate files** in any folder (including subfolders)
- **Identify which files are identical** copies of each other
- **Free up storage space** by knowing which files can be safely deleted

## 🛠️ Prerequisites

### 1. Install Python

First, make sure Python is installed on your computer:

**Windows:**
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. ✅ **IMPORTANT:** Check the box "Add Python to PATH" during installation!
4. Click "Install Now"

**Mac:**
1. Open Terminal
2. Type: `python3 --version`
3. If not installed, download from [python.org](https://www.python.org/downloads/)

**Linux:**
```bash
sudo apt update
sudo apt install python3
```

### 2. VS Code Extensions (Recommended)

Install these extensions in VS Code for the best experience:

| Extension | Publisher | What It Does |
|-----------|-----------|-------------|
| **Python** | Microsoft | Run Python code, debugging, syntax highlighting |
| **Pylance** | Microsoft | Smart code suggestions and error detection |

**How to install extensions:**
1. Open VS Code
2. Click the **Extensions** icon (4 squares) on the left sidebar (or press `Ctrl+Shift+X`)
3. Search for "Python" → Click **Install**
4. Search for "Pylance" → Click **Install**

## 🚀 How to Run the Script

### Method 1: Using VS Code (Recommended for Beginners)

1. **Open the project folder in VS Code:**
   - File → Open Folder → Select the folder containing `duplicate_finder.py`

2. **Open the script:**
   - Click on `duplicate_finder.py` in the file explorer

3. **Run the script:**
   - Click the **▶️ Play button** in the top-right corner
   - OR press `F5`
   - OR right-click and select "Run Python File in Terminal"

4. **Enter the folder path when prompted:**
   ```
   📂 Enter folder path: C:\Users\YourName\Downloads
   ```

### Method 2: Using Command Line / Terminal

**Windows (Command Prompt or PowerShell):**
```cmd
cd path\to\your\project
python duplicate_finder.py
```

**Mac/Linux (Terminal):**
```bash
cd /path/to/your/project
python3 duplicate_finder.py
```

## 📖 How the Script Works

Here's a simple explanation of the process:

```
┌─────────────────────────────────────────────────────────────┐
│  1. USER INPUT                                              │
│     You enter a folder path to scan                         │
├─────────────────────────────────────────────────────────────┤
│  2. FILE SCANNING                                           │
│     CloneX walks through ALL files in the folder            │
│     (including files in subfolders)                         │
├─────────────────────────────────────────────────────────────┤
│  3. HASH CALCULATION                                        │
│     For each file, calculates a SHA256 "fingerprint"        │
│     (Two identical files = same fingerprint)                │
├─────────────────────────────────────────────────────────────┤
│  4. DUPLICATE DETECTION                                     │
│     Groups files by their fingerprint                       │
│     If 2+ files share a fingerprint → They're duplicates!   │
├─────────────────────────────────────────────────────────────┤
│  5. RESULTS                                                 │
│     Shows you which files are duplicates                    │
│     Suggests which ones you can delete                      │
└─────────────────────────────────────────────────────────────┘
```

## 📝 Example Output

```
============================================================
   📁 CloneX
   Find and remove duplicate files to free up space!
============================================================

📂 Enter folder path: C:\Users\John\Downloads

🔍 Scanning files...

✅ Finished! Scanned 150 files total.

============================================================
📋 DUPLICATE FILES FOUND:
============================================================

🔴 Duplicate Group #1:
   (These 3 files are identical copies)
--------------------------------------------------
   ✅ KEEP: C:\Users\John\Downloads\photo.jpg
   ❌ DUPLICATE: C:\Users\John\Downloads\photo (1).jpg
   ❌ DUPLICATE: C:\Users\John\Downloads\backup\photo.jpg

🔴 Duplicate Group #2:
   (These 2 files are identical copies)
--------------------------------------------------
   ✅ KEEP: C:\Users\John\Downloads\document.pdf
   ❌ DUPLICATE: C:\Users\John\Downloads\old\document.pdf

============================================================
📊 SUMMARY:
   • Found 2 group(s) of duplicates
   • 3 file(s) can be safely deleted

💡 TIP: You can delete the files marked with ❌ to free up space!
============================================================
```

## 🧪 Test the Script

Want to test the script? Create some duplicate files:

1. **Create a test folder:**
   ```
   test_folder/
   ├── file1.txt        (contains: "Hello World")
   ├── file2.txt        (contains: "Hello World")  ← Duplicate!
   ├── file3.txt        (contains: "Different text")
   └── subfolder/
       └── file4.txt    (contains: "Hello World")  ← Duplicate!
   ```

2. **Run the script and enter:** `test_folder`

3. **Expected result:** file1.txt, file2.txt, and file4.txt will be flagged as duplicates!

## 🔧 Troubleshooting

### "Python is not recognized" error
- **Solution:** Reinstall Python and make sure to check "Add Python to PATH"

### "Permission denied" error
- **Solution:** Some system files can't be read. The script will skip them automatically.

### "Folder does not exist" error
- **Solution:** Double-check the path. Use copy-paste from File Explorer.

### Script runs but finds no duplicates
- **Solution:** There might genuinely be no duplicates! Or try scanning a larger folder.

## 📚 Key Python Concepts Used

This script demonstrates several important Python concepts:

| Concept | What It Does | Where Used |
|---------|--------------|------------|
| `os` module | Navigate files and folders | `os.walk()`, `os.path.join()` |
| `hashlib` module | Create file fingerprints | `hashlib.sha256()` |
| Dictionaries | Store hash → file mappings | `hash_dictionary = {}` |
| Functions | Organize code into reusable blocks | `calculate_file_hash()` |
| File handling | Read file contents | `with open(file, 'rb')` |
| Error handling | Handle problems gracefully | `try/except` blocks |

## ⚠️ Important Notes

1. **CloneX only FINDS duplicates** - it does NOT delete them automatically
2. **Always review the results** before deleting any files
3. **The script is safe** - it only reads files, never modifies them
4. **Large folders take time** - scanning thousands of files may take a few minutes

## 📄 License

Free to use for learning purposes! 🎓

---

**Wishing you all the best my friend 😎👍**
