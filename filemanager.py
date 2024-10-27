import os
import shutil

def organize_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            ext = filename.split('.')[-1]
            folder = os.path.join(directory, ext)
            os.makedirs(folder, exist_ok=True)
            shutil.move(file_path, folder)
    print("Files organized.")

directory = "path/to/your/directory"
organize_files(directory)
