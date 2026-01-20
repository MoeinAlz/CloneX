# CloneX

A simple tool that finds duplicate files on your computer.

## What's This About?

You know how your Downloads folder gets out of control? Files everywhere, half of them probably duplicates you forgot about. I got tired of manually checking, so I made this.

CloneX scans through your folders, compares files using SHA256 hashing, and tells you which ones are identical. Then you can decide what to delete.

## Before You Start

### Get Python

**Windows:**
1. Grab it from [python.org](https://www.python.org/downloads/)
2. During install, check "Add Python to PATH" - this is important
3. Click Install

**Mac/Linux:**
```bash
python3 --version
```
If it's not there, get it from python.org

### VS Code Setup (Optional but Nice)

If you're using VS Code, these extensions make life easier:
- **Python** by Microsoft
- **Pylance** by Microsoft

Just search for them in the Extensions tab and hit Install.

## Running It

### The Easy Way (VS Code)
1. Open the folder with `duplicate_finder.py`
2. Hit the play button in the top right
3. Type in the folder you want to scan

### Command Line
```bash
python duplicate_finder.py
# or on Mac/Linux
python3 duplicate_finder.py
```

## How It Works

Pretty straightforward:

1. **You give it a folder** - Could be Downloads, Documents, wherever
2. **It goes through every file** - Including stuff in subfolders
3. **Creates a fingerprint for each file** - Using SHA256, so it's accurate
4. **Groups the matches** - Same fingerprint = same file
5. **Shows you the duplicates** - You decide what to do with them

## What You'll See

```
============================================================
   CloneX
   Find and remove duplicate files to free up space!
============================================================

Enter folder path: C:\Users\You\Downloads

Scanning files...

Finished! Scanned 150 files total.

============================================================
DUPLICATE FILES FOUND:
============================================================

Duplicate Group #1:
   (These 3 files are identical copies)
--------------------------------------------------
   KEEP: C:\Users\You\Downloads\photo.jpg
   DUPLICATE: C:\Users\You\Downloads\photo (1).jpg
   DUPLICATE: C:\Users\You\Downloads\backup\photo.jpg

SUMMARY:
   Found 2 group(s) of duplicates
   3 file(s) can be safely deleted
```

## Want to Test It First?

Create a test folder with some duplicate files:

```
test_folder/
  file1.txt (write "hello" in it)
  file2.txt (write "hello" in it too)
  file3.txt (write something different)
```

Run the script on test_folder. It should catch file1 and file2 as duplicates.

## Common Issues

**"Python is not recognized"**
You probably didn't check "Add to PATH" during install. Reinstall Python and make sure to check that box.

**"Permission denied" on some files**
Some system files are protected. The script skips these automatically, no worries.

**"Folder does not exist"**
Double-check your path. Copy it directly from File Explorer if you're unsure.

## Good to Know

- This only finds duplicates - it won't delete anything without you saying so
- Large folders take a bit longer, that's normal
- It's safe to run - nothing gets modified

---

Questions? Issues? Let me know.