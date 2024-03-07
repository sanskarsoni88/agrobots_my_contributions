import xml.etree.ElementTree as ET
from PIL import Image, ImageFilter
import os

def resize_annotations(xml_file, resize_factor_x, resize_factor_y):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for obj in root.findall('object'):
        if obj.find('name').text == 'maize':
            bndbox = obj.find('bndbox')
            bndbox.find('xmin').text = str(int(int(bndbox.find('xmin').text) // resize_factor_x))
            bndbox.find('ymin').text = str(int(int(bndbox.find('ymin').text) // resize_factor_x))
            bndbox.find('xmax').text = str(int(int(bndbox.find('xmax').text) // resize_factor_x))
            bndbox.find('ymax').text = str(int(int(bndbox.find('ymax').text) // resize_factor_x))

    return tree

def process_images_and_annotations(source_folder, dest_folder, new_width):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for file in os.listdir(source_folder):
        if file.endswith('.jpg'):
            image_path = os.path.join(source_folder, file)
            with Image.open(image_path) as img:
                # Calculate resize factors
                original_width, original_height = img.size
                resize_factor_x = original_width / new_width

                # Apply a smoothing filter and resize
                img = img.filter(ImageFilter.SMOOTH)
                new_height = int(original_height / resize_factor_x)
                resized_img = img.resize((new_width, new_height), Image.LANCZOS)
                resized_img.save(os.path.join(dest_folder, file))

            # Process corresponding XML file
            xml_file = file.replace('.jpg', '.xml')
            xml_path = os.path.join(source_folder, xml_file)
            if os.path.exists(xml_path):
                tree = resize_annotations(xml_path, resize_factor_x, resize_factor_x)
                tree.write(os.path.join(dest_folder, xml_file))

# Replace these paths with your actual folder paths
source_folder = 'C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/refined_dataset/dirt'
dest_folder = 'C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/refined_dataset/dirt_256'
new_width = 256  # The new width for all images

process_images_and_annotations(source_folder, dest_folder, new_width)
