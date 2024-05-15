import os
import random

def delete_half_files(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Calculate the number of files to delete
    num_files_to_delete = len(files) *3 // 4
    
    # Randomly select files to delete
    files_to_delete = random.sample(files, num_files_to_delete)
    
    # Delete the selected files
    for file_name in files_to_delete:
        file_path = os.path.join(folder_path, file_name)
        os.remove(file_path)
        print(f"Deleted: {file_path}")

folder_path = "./train"
delete_half_files(folder_path)