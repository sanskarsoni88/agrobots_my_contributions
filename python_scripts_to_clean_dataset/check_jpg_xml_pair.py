import os
import shutil

def copy_matching_files(folder_a, folder_b):
    # Get all JPG files in folder_a
    jpg_files = [file for file in os.listdir(folder_a) if file.lower().endswith('.jpg')]

    for jpg_file in jpg_files:
        # Check if corresponding XML file exists
        xml_file = os.path.splitext(jpg_file)[0] + '.xml'
        if xml_file in os.listdir(folder_a):
            # If XML file exists, copy both JPG and XML to folder_b
            shutil.copy(os.path.join(folder_a, jpg_file), folder_b)
            shutil.copy(os.path.join(folder_a, xml_file), folder_b)

# Replace these paths with the actual paths of your folders
folder_a_path = 'C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/dataset'
folder_b_path = 'C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/refined_dataset'

copy_matching_files(folder_a_path, folder_b_path)
