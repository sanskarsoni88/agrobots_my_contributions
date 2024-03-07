# To check how many files in location_a are in location_b

import os

def get_files_in_directory(directory):
    # Get a list of files in the specified directory
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def compare_directories(location_a, location_b):
    files_location_a = get_files_in_directory(location_a)
    files_location_b = get_files_in_directory(location_b)
    
    common_files = set(files_location_a).intersection(files_location_b)
    return len(common_files)

# Replace these paths with your directory paths
location_a = 'C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/dataset'
location_b = 'C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/refined_dataset'


common_files_count = compare_directories(location_a, location_b)
print(f'The number of files common to both directories: {common_files_count}')
