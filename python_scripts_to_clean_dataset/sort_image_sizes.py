import os
from PIL import Image
import shutil

# Define the directory path where the images are stored
image_directory = 'C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/refined_dataset'

# Define the target directories for each original image size
target_directories = {
    (2048, 1536): 'C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/refined_dataset/2048x1536',
    (1440, 1080): 'C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/refined_dataset/1440x1080',
    (1024, 768): 'C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/refined_dataset/1024x768',
    (632, 632): 'C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/refined_dataset/632x632',
    (2448, 2048): 'C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/refined_dataset/2448x2048'
}

# Function to copy images and corresponding XML files to the target directories based on their original size
def sort_images_and_xml_by_dimensions(source_dir, target_dirs):
    for filename in os.listdir(source_dir):
        if filename.lower().endswith('.jpg'):  # Check for .jpg files
            image_path = os.path.join(source_dir, filename)
            xml_path = os.path.splitext(image_path)[0] + '.xml'  # Corresponding XML file path

            # Get the image dimensions
            with Image.open(image_path) as img:
                image_dimensions = img.size

            # Copy the file to the corresponding directory if the dimensions match
            if image_dimensions in target_dirs:
                shutil.copy2(image_path, os.path.join(target_dirs[image_dimensions], filename))
                # Check if the corresponding XML file exists and copy it
                if os.path.exists(xml_path):
                    shutil.copy2(xml_path, os.path.join(target_dirs[image_dimensions], os.path.basename(xml_path)))
            else:
                print(f"No target directory for image dimensions {image_dimensions}. File '{filename}' remains unsorted.")

# Call the function with the path to your image directory
sort_images_and_xml_by_dimensions(image_directory, target_directories)
