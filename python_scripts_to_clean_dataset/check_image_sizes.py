import os
from PIL import Image
from collections import Counter

# Function to get image sizes and frequencies in a folder
def get_image_sizes_freq(folder_path):
    sizes_freq = Counter()

    # List all files in the directory
    for file_name in os.listdir(folder_path):
        # Check for .jpg files
        if file_name.lower().endswith('.jpg'):
            try:
                # Open the image and get its size
                with Image.open(os.path.join(folder_path, file_name)) as img:
                    sizes_freq[img.size] += 1
            except IOError as e:
                # If the file couldn't be opened, it might not be an image or might be corrupted
                print(f"Could not open {file_name} as an image. Error: {e}")

    return sizes_freq

# Replace 'your_folder_path' with the actual path to your folder containing the images
your_folder_path = 'C:/Users/ASUS/Desktop/notes/agrobots/datasets/DB_Mendeley/refined_dataset/256x215'

# Get the sizes and frequencies of the images
image_sizes_and_freq = get_image_sizes_freq(your_folder_path)

# Print out the sizes and their frequencies
for size, freq in image_sizes_and_freq.items():
    print(f"Image size: {size}, Frequency: {freq}")
