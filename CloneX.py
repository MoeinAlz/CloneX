"""
📁 CloneX
A simple script that finds duplicate files using SHA256 hashing.
"""

import os
import hashlib


def calculate_file_hash(file_path):
    """Calculate SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    
    try:
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(65536), b''):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    
    except PermissionError:
        print(f"  ⚠️  Cannot read (permission denied): {file_path}")
        return None
    except Exception as error:
        print(f"  ⚠️  Error reading file: {file_path} - {error}")
        return None


def find_duplicates(folder_path):
    """Scan a folder and find all duplicate files."""
    hash_dictionary = {}
    files_scanned = 0
    
    print("\n🔍 Scanning files...\n")
    
    for current_folder, subfolders, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(current_folder, filename)
            file_hash = calculate_file_hash(file_path)
            
            if file_hash is None:
                continue
            
            if file_hash in hash_dictionary:
                hash_dictionary[file_hash].append(file_path)
            else:
                hash_dictionary[file_hash] = [file_path]
            
            files_scanned += 1
            
            if files_scanned % 100 == 0:
                print(f"  📄 Scanned {files_scanned} files...")
    
    print(f"\n✅ Finished! Scanned {files_scanned} files total.\n")
    return hash_dictionary


def display_duplicates(hash_dictionary):
    """Display duplicate files to the user."""
    duplicates_found = False
    duplicate_groups = 0
    total_duplicate_files = 0
    
    print("=" * 60)
    print("📋 DUPLICATE FILES FOUND:")
    print("=" * 60)
    
    for file_hash, file_list in hash_dictionary.items():
        if len(file_list) > 1:
            duplicates_found = True
            duplicate_groups += 1
            total_duplicate_files += len(file_list) - 1
            
            print(f"\n🔴 Duplicate Group #{duplicate_groups}:")
            print(f"   (These {len(file_list)} files are identical copies)")
            print("-" * 50)
            
            for index, file_path in enumerate(file_list):
                if index == 0:
                    print(f"   ✅ KEEP: {file_path}")
                else:
                    print(f"   ❌ DUPLICATE: {file_path}")
    
    print("\n" + "=" * 60)
    if duplicates_found:
        print(f"📊 SUMMARY:")
        print(f"   • Found {duplicate_groups} group(s) of duplicates")
        print(f"   • {total_duplicate_files} file(s) can be safely deleted")
        print(f"\n💡 TIP: You can delete the files marked with ❌ to free up space!")
    else:
        print("🎉 Great news! No duplicate files were found.")
    print("=" * 60)


def main():
    """Main function to run the duplicate finder."""
    print("\n" + "=" * 60)
    print("   📁 CloneX")
    print("   Find and remove duplicate files to free up space!")
    print("=" * 60)
    
    print("\nEnter the path to the folder you want to scan.")
    print("Examples:")
    print("  • Windows: C:\\Users\\YourName\\Downloads")
    print("  • Mac/Linux: /home/yourname/Downloads")
    print("  • Or just type a folder name like: test_folder")
    
    folder_path = input("\n📂 Enter folder path: ").strip()
    folder_path = folder_path.strip('"').strip("'")
    
    if not os.path.exists(folder_path):
        print(f"\n❌ Error: The folder '{folder_path}' does not exist!")
        print("   Please check the path and try again.")
        return
    
    if not os.path.isdir(folder_path):
        print(f"\n❌ Error: '{folder_path}' is a file, not a folder!")
        print("   Please enter a folder path.")
        return
    
    hash_dictionary = find_duplicates(folder_path)
    display_duplicates(hash_dictionary)
    
    print("\n👋 Thank you for using CloneX!\n")


if __name__ == "__main__":
    main()