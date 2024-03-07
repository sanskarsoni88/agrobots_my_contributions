from PIL import Image
import os
import xml.etree.ElementTree as ET

def update_annotation_size(xml_file_path, output_xml_path):
    """
    Update the width and height in the XML file to 256 and save to the output folder.
    """
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Find the size tag and update width and height
    size_tag = root.find('size')
    size_tag.find('width').text = '256'
    size_tag.find('height').text = '256'

    # Save the updated XML to the output folder
    tree.write(output_xml_path)

def pad_image_with_dirt(source_image_path, dirt_image_path, output_image_path, source_xml_path, output_xml_path):
    """
    Pad an image with a "dirt" image at the bottom to reach a size of 256x256 and update its XML annotation.
    """
    with Image.open(source_image_path) as source_img, Image.open(dirt_image_path) as dirt_img:
        source_width, source_height = source_img.size
        padding_height = 256 - source_height

        if padding_height > 0:
            dirt_padding = dirt_img.crop((0, 256 - padding_height, 256, 256))
            padded_img = Image.new('RGB', (256, 256), (255, 255, 255))
            padded_img.paste(source_img, (0, 0))
            padded_img.paste(dirt_padding, (0, source_height))
            padded_img.save(output_image_path)
        else:
            source_img.save(output_image_path)

    # Update the XML file size and save it to the output folder
    update_annotation_size(source_xml_path, output_xml_path)

def pad_images_in_folder(source_folder, dirt_image_path, dest_folder):
    for file in os.listdir(source_folder):
        if file.endswith('.jpg'):
            source_image_path = os.path.join(source_folder, file)
            output_image_path = os.path.join(dest_folder, file)
            source_xml_path = os.path.splitext(source_image_path)[0] + '.xml'
            output_xml_path = os.path.join(dest_folder, os.path.splitext(file)[0] + '.xml')

            pad_image_with_dirt(source_image_path, dirt_image_path, output_image_path, source_xml_path, output_xml_path)


# Replace these paths with your actual folder paths
source_folder = 'C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/refined_dataset/256x214'
dirt_image_path = 'C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/refined_dataset/dirt_256/dirt_256.jpg'
dest_folder = 'C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/refined_dataset/256x256/256x214'


pad_images_in_folder(source_folder, dirt_image_path, dest_folder)



