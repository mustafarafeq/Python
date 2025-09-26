import os
import shutil

# 1. Define the folder you want to organize
# The tilde (~) is a shortcut for your home directory on macOS.
downloads_folder = os.path.expanduser('~/Downloads')

# 2. Define your file categories and which extensions belong to them
FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".rtf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".tiff"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mov", ".avi", ".flv"],
    "Installers": [".dmg", ".pkg"],
    "Code": [".py", ".sh", ".js"],
    "Other": [] # Default for anything not matched
}

# 3. Create a function to find the right category for a file
def get_category(filename):
    file_extension = os.path.splitext(filename)[1].lower()
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension in extensions:
            return category
    return "Other"

# 4. Loop through every file and move it to the right place
def organize_downloads():
    print(f"Starting to organize files in: {downloads_folder}")
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)

        # Skip directories to avoid issues and skip the script itself
        if os.path.isdir(file_path) or filename == 'organize_downloads.py':
            continue

        # Find the destination category and create the folder if it doesn't exist
        category = get_category(filename)
        destination_folder = os.path.join(downloads_folder, category)

        # Create the destination folder if it doesn't exist
        os.makedirs(destination_folder, exist_ok=True)

        # Move the file
        try:
            shutil.move(file_path, destination_folder)
            print(f"Moved: {filename} -> {category}/")
        except shutil.Error as e:
            print(f"Could not move {filename}: {e}")

    print("Organization complete!")

# 5. Run the function
if __name__ == "__main__":
    organize_downloads()
