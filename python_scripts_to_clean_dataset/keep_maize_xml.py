import xml.etree.ElementTree as ET
import os

def clean_annotations(folder_path):
    for file in os.listdir(folder_path):
        if file.endswith('.xml'):
            file_path = os.path.join(folder_path, file)
            tree = ET.parse(file_path)
            root = tree.getroot()

            # Iterate through all object elements and remove those not named "maize"
            objects = root.findall('object')
            for obj in objects:
                name = obj.find('name').text
                if name != 'maize':
                    root.remove(obj)

            # Save the modified XML back to the file
            tree.write(file_path)

# Replace 'your_folder_path' with the path to your folder containing XML files
clean_annotations('C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/refined_dataset')
