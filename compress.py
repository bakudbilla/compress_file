import os
import shutil
import tarfile
import zipfile
from datetime import datetime
#Get the name of the folder
def compress_folder(folder_path, compress_type):
    try:
        folder_name = os.path.basename(folder_path)
        #setting date to the date format
        current_date = datetime.now().strftime("%Y_%m_%d")
        compressed_file_name = f"{folder_name}_{current_date}.{compress_type}"
#setting the file types
        if compress_type == "zip":
            with zipfile.ZipFile(compressed_file_name, 'w') as zip_file:
                for folder_root, _, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(folder_root, file)
                        zip_file.write(file_path, os.path.relpath(file_path, folder_path))

        elif compress_type == "tar":
            with tarfile.open(compressed_file_name, 'w') as tar_file:
                tar_file.add(folder_path, arcname=os.path.basename(folder_path))

        elif compress_type == "tgz":
            compressed_file_name = f"{folder_name}_{current_date}.tar.gz"
            with tarfile.open(compressed_file_name, 'w:gz') as tar_file:
                tar_file.add(folder_path, arcname=os.path.basename(folder_path))

        else:
            print("Invalid compression type. Supported types are zip, tar, and tgz.")
            return False

        print(f"Compression successful. Compressed file saved as {compressed_file_name}")
        return True

    except Exception as e:
        print(f"Compression failed. Error: {str(e)}")
        return False
#prompt user to enter folder path
def main():
    folder_path = input("Enter the path of the folder to compress: ")
    
    if not os.path.exists(folder_path):
        print("Error: Folder not found.")
        return

    compress_types = ["zip", "tar", "tgz"]
    print("Available compressed file types: ", ", ".join(compress_types))

    compress_type = input("Select the desired compressed file type: ").lower()
#returns a message if code is correct or not
    if compress_type not in compress_types:
        print("Invalid compression type. Supported types are zip, tar, and tgz.")
        return

    compress_folder(folder_path, compress_type)

if __name__ == "__main__":
    main()