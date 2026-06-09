import time
import shutil
from pathlib import Path


def get_path_from_user(prompt, default_name, task):
    custom = input("Enter custom path for " + prompt + "? (y/n) -- ").lower()
    if custom == "y":
        return Path(input("Custom path for " + prompt + " -- "))
    else:
        print("Task " + task + " uses default path: " + default_name)
        return Path(default_name)


def pylevel_main():
    MaxNumber = 19
    t1tt3v = 0
    t5v = 0
    t7v = 0
    while True:
        time.sleep(1)
        print("--- Select an action: ---")
        print("1. Count occurrences")
        print("2. Find position of first occurrence")
        print("3. Find all occurrence positions")
        print("4. Check if string is integer or float")
        print("5. Create a new text file and write a string")
        print("6. Read file contents and display")
        print("7. Append new string to end of existing file")
        print("8. Check if a file exists at given path")
        print("9. Check if a directory exists at given path")
        print("10. Delete a file")
        print("11. Create a new directory")
        print("12. Delete a directory")
        print("13. Rename a file or directory")
        print("14. Copy a file to a new location")
        print("15. Get full path to a file")
        print("16. Get file name from full path")
        print("17. Get file extension")
        print("18. Get parent directory of a file")
        print("19. List all files in current directory")
        print("exit or 0. Exit")
        choice = input("Which? -- ").lower()
        if t1tt3v == 0 and choice in ["1", "2", "3"]:
            MainString = input("Main String -- ")
            SubString = input("Sub String -- ")
            if SubString == "":
                print("No")
        if choice == "1":
            print(MainString.count(SubString))
            t1tt3v += 1
        elif choice == "2":
            print(MainString.find(SubString) + 1)
            t1tt3v += 1
        elif choice == "3":
            Poses = []
            start_search = 0
            while True:
                pos = MainString.find(SubString, start_search)
                if pos == -1:
                    break
                Poses.append(pos + 1)
                start_search = pos + len(SubString)
            print("All occurrence positions:", Poses)
            t1tt3v += 1
        elif choice == "4":
            Value = input("Enter a word or Number -- ")
            try:
                float(Value)
                if "." in Value or "e" in Value.lower():
                    print("That is a decimal")
                else:
                    print("That is an integer!")
            except ValueError:
                print("That is a word!")
        elif choice == "5":
            task5_path = Path("task5tt7.txt")
            t5v += 1
            if t5v > 1:
                new_text = "This text was written to file by task 5 (" + str(t5v) + " times)."
            else:
                new_text = "This text was written to file by task 5."
            task5_path.write_text(new_text, encoding="utf-8")
            print("Text successfully written.")
        elif choice == "6":
            task6_path = Path("task5tt7.txt")
            if not task6_path.exists():
                task6_path.write_text("This text was written to file by task 6.", encoding="utf-8")
            content = task6_path.read_text(encoding="utf-8")
            print(content)
        elif choice == "7":
            task7_path = Path("task5tt7.txt")
            t7v += 1
            t7v2 = "This text was appended to file by task 7 (" + str(t7v) + " times)."
            with open(task7_path, "a", encoding="utf-8") as f:
                f.write(t7v2 + "\n")
        elif choice == "8":
            task8_path = get_path_from_user("file", "task5tt7.txt", "8")
            if task8_path.is_file():
                print("Yes, '" + str(task8_path) + "' exists and is a file.")
            else:
                print("File not found at specified path.")

        elif choice == "9":
            task9_path = get_path_from_user("directory", "task9t11", "9")
            if task9_path.is_dir():
                print("Yes, '" + str(task9_path) + "' exists and is a directory.")
            else:
                print("Directory not found at specified path.")

        elif choice == "10":
            task10_path = get_path_from_user("deletion", "task5tt7.txt", "10")
            if task10_path.is_file():
                confirm = input("Delete file '" + str(task10_path) + "'? (y/n) -- ").lower()
                if confirm == "y":
                    task10_path.unlink()
                    print("File successfully deleted.")
                else:
                    print("Operation cancelled.")
            else:
                print("File not found at specified path.")
        elif choice == "11":
            task11_path = Path("task9t11")
            if task11_path.exists():
                print("Directory already exists")
            else:
                task11_path.mkdir()
        elif choice == "12":
            task12_path = get_path_from_user("deletion", "task9t11", "12")
            if task12_path.is_dir():
                confirm = input("Delete directory '" + str(task12_path) + "'? (y/n) -- ").lower()
                if confirm == "y":
                    try:
                        task12_path.rmdir()
                        print("Directory successfully deleted.")
                    except OSError:
                        confirm_clear = input("Directory not empty. Clear and delete? (y/n) -- ").lower()
                        if confirm_clear == "y":
                            shutil.rmtree(task12_path)
                            print("Directory and all contents deleted.")
                        else:
                            print("Operation cancelled.")
                else:
                    print("Operation cancelled.")
            else:
                print("Directory not found at specified path.")
        elif choice == "13":
            source_path = get_path_from_user("renaming", "task5tt7.txt", "13")
            if not source_path.exists():
                print("Source object not found.")
                continue
            dest_str = input("Enter new name/path for '" + source_path.name + "': ")
            destination_path = Path(dest_str)
            if destination_path.exists():
                confirm = input("'" + str(destination_path) + "' already exists. Replace? (y/n) -- ").lower()
                if confirm != 'y':
                    print("Operation cancelled.")
                    continue
            try:
                source_path.rename(destination_path)
                print("Success! '" + str(source_path) + "' renamed to '" + str(destination_path) + "'.")
            except Exception as e:
                print("Error during rename: " + str(e))
        elif choice == "14":
            src_path = get_path_from_user("copying", "task5tt7.txt", "14")
            if not src_path.is_file():
                print("Source file not found.")
                continue
            dst_str = input("Enter destination path (including new filename): ")
            dst_path = Path(dst_str)
            if dst_path.exists():
                confirm = input("'" + str(dst_path) + "' already exists. Replace? (y/n) -- ").lower()
                if confirm != 'y':
                    print("Operation cancelled.")
                    continue
            try:
                shutil.copy(src_path, dst_path)
                print("Success! File copied to '" + str(dst_path) + "'.")
            except Exception as e:
                print("Error during copy: " + str(e))
        elif choice == "15":
            path = get_path_from_user("full path", "task5tt7.txt", "15")
            print("Absolute path: " + str(path.resolve()))

        elif choice == "16":
            path = get_path_from_user("file name", "task5tt7.txt", "16")
            print("File/directory name: " + path.name)

        elif choice == "17":
            path = get_path_from_user("file extension", "task5tt7.txt", "17")
            print("Extension: " + path.suffix)

        elif choice == "18":
            path = get_path_from_user("parent directory", "task5tt7.txt", "18")
            print("Path to parent directory: " + str(path.parent))

        elif choice == "19":
            current_dir = Path.cwd()
            print("Files in '" + str(current_dir) + "':")
            for item in current_dir.iterdir():
                if item.is_file():
                    print(item.name)
        elif choice == "exit" or choice == "0":
            print("Exiting program.")
            time.sleep(0.2)
            break
        else:
            if choice.isdigit():
                print("Invalid choice. Please enter a number from 1 to " + str(MaxNumber) + ".")
            elif choice != "exit":
                print("Invalid input. Please enter a number from 1 to " + str(MaxNumber) + " or 'exit'.")
