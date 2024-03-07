import xml.etree.ElementTree as ET
from PIL import Image
import os

def calculate_intersection_area(original_box, crop_box):
    # Determine the overlap between the original box and the crop box
    x_overlap = max(0, min(original_box[2], crop_box[2]) - max(original_box[0], crop_box[0]))
    y_overlap = max(0, min(original_box[3], crop_box[3]) - max(original_box[1], crop_box[1]))
    return x_overlap * y_overlap

def adjust_annotations_for_crop(xml_file, crop_box, new_area):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for obj in root.findall('object'):
        bndbox = obj.find('bndbox')
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)

        original_box = (xmin, ymin, xmax, ymax)
        original_area = (xmax - xmin) * (ymax - ymin)
        intersection_area = calculate_intersection_area(original_box, crop_box)

        # Check if the intersection area meets the new_area requirement
        if intersection_area / original_area >= new_area:
            # Adjust the coordinates of the annotation to the new cropped image
            bndbox.find('xmin').text = str(max(0, xmin - crop_box[0]))
            bndbox.find('ymin').text = str(max(0, ymin - crop_box[1]))
            bndbox.find('xmax').text = str(min(crop_box[2] - crop_box[0], xmax - crop_box[0]))
            bndbox.find('ymax').text = str(min(crop_box[3] - crop_box[1], ymax - crop_box[1]))
        else:
            # Remove the object if the area condition is not met
            root.remove(obj)

    return tree

def crop_images_and_annotations(source_folder, dest_folder, var_height, new_area):
    for file in os.listdir(source_folder):
        if file.endswith('.jpg'):
            image_path = os.path.join(source_folder, file)
            xml_path = os.path.splitext(image_path)[0] + '.xml'
            with Image.open(image_path) as img:
                width, height = img.size

                # Crop specifications
                crop_boxes = [
                    (0, 0, width, 110),  # Top crop
                    (0, (height // 2) - 55, width, (height // 2) + 55),  # Middle crop
                    (0, height - 110, width, height)  # Bottom crop
                ]

                for i, crop_box in enumerate(crop_boxes):
                    # Crop the image
                    cropped_img = img.crop(crop_box)
                    cropped_img.save(os.path.join(dest_folder, f"{os.path.splitext(os.path.basename(image_path))[0]}_crop_{i}.jpg"))

                    # Adjust and filter the annotations if XML exists
                    if os.path.exists(xml_path):
                        tree = adjust_annotations_for_crop(xml_path, crop_box, new_area)
                        tree.write(os.path.join(dest_folder, f"{os.path.splitext(os.path.basename(image_path))[0]}_crop_{i}.xml"))

# Replace these paths with your actual folder paths
source_folder = 'C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/refined_dataset/256x192/1440x1080'
dest_folder = 'C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/refined_dataset/test_crop_annotation'
var_height = 110  # Height for cropping
new_area = 0.8  # Minimum area threshold to keep an annotation

crop_images_and_annotations(source_folder, dest_folder, var_height, new_area)
