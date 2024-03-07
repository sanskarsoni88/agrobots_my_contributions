from PIL import Image
import os

def crop_image(image_path, dest_folder, var_height):
    with Image.open(image_path) as img:
        width, height = img.size

        # Ensure the variable height is not less than 110 to avoid errors in cropping
        if var_height < 110:
            raise ValueError("Image height must be at least 110 pixels")

        # Crop specifications
        top_crop = (0, 0, width, 110)
        middle_crop = (0, (height // 2) - 55, width, (height // 2) + 55)
        bottom_crop = (0, height - 110, width, height)

        # Perform the cropping operations
        img.crop(top_crop).save(os.path.join(dest_folder, f"{os.path.splitext(os.path.basename(image_path))[0]}_top.jpg"))
        img.crop(middle_crop).save(os.path.join(dest_folder, f"{os.path.splitext(os.path.basename(image_path))[0]}_middle.jpg"))
        img.crop(bottom_crop).save(os.path.join(dest_folder, f"{os.path.splitext(os.path.basename(image_path))[0]}_bottom.jpg"))

def crop_images_in_folder(source_folder, dest_folder):
    for file in os.listdir(source_folder):
        if file.endswith('.jpg'):
            image_path = os.path.join(source_folder, file)
            crop_image(image_path, dest_folder, Image.open(image_path).size[1])

# Replace these paths with your actual folder paths
source_folder = 'C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/refined_dataset/256x192/1440x1080'
dest_folder = 'C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/refined_dataset/test_crop'

crop_images_in_folder(source_folder, dest_folder)
