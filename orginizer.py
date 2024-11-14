import os
import shutil

def organize_files(directory):
    """Organize files in the specified directory by their extensions."""
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = filename.split('.')[-1]
            folder_name = os.path.join(directory, file_extension)

            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

            shutil.move(os.path.join(directory, filename), os.path.join(folder_name, filename))
            print(f"Moved: {filename} to {folder_name}")

def main():
    directory = input("Enter the directory path to organize files: ")
    if os.path.exists(directory):
        organize_files(directory)
        print("Files organized successfully.")
    else:
        print("The specified directory does not exist.")

if __name__ == "__main__":
    main()
