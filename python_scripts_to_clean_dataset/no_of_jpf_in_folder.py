import os

def count_jpg_files(folder_a):
    jpg_count = len([file for file in os.listdir(folder_a) if file.lower().endswith('.jpg')])
    return jpg_count

# Replace this path with the actual path of your folder
folder_a_path = 'C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/dataset'
folder_b_path = 'C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/refined_dataset'

jpg_file_count = count_jpg_files(folder_a_path)
print(f'The number of JPG files in dataset: {jpg_file_count}')

jpg_file_count_refined = count_jpg_files(folder_b_path)
print(f'The number of JPG files in refined_dataset: {jpg_file_count_refined}')