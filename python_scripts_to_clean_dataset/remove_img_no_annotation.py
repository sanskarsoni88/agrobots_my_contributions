import xml.etree.ElementTree as ET
import os

def has_annotations(xml_file):
    """Check if the XML file has any object annotations."""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    return len(root.findall('object')) > 0

def remove_images_without_annotations(source_folder):
    for file in os.listdir(source_folder):
        if file.endswith('.jpg'):
            image_path = os.path.join(source_folder, file)
            xml_path = os.path.splitext(image_path)[0] + '.xml'

            # Check if the corresponding XML file has annotations
            if os.path.exists(xml_path) and not has_annotations(xml_path):
                # If no annotations, remove the image and XML file
                os.remove(image_path)
                os.remove(xml_path)

# Replace this path with your actual folder path
source_folder = 'C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/refined_dataset/test_crop_annotation'

remove_images_without_annotations(source_folder)
