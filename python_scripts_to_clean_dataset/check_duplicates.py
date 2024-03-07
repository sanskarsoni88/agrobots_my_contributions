import os

def find_duplicate_files(directory):
    file_dict = {}
    duplicates = []

    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_size = os.path.getsize(file_path)
            if (filename, file_size) in file_dict:
                duplicates.append((file_dict[(filename, file_size)], file_path))
            else:
                file_dict[(filename, file_size)] = file_path

    return duplicates

# Replace this path with the directory you want to check for duplicates
folder_path = 'C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/dataset'

duplicate_files = find_duplicate_files(folder_path)

if duplicate_files:
    print("Duplicate files found:")
    for duplicate_pair in duplicate_files:
        print(f"Original: {duplicate_pair[0]} - Duplicate: {duplicate_pair[1]}")
else:
    print("No duplicate files found in the directory.")
