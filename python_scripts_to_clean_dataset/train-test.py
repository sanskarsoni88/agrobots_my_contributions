import os
import shutil
from random import shuffle

# Define your directories
images_dir = 'C:/Users/ASUS/Desktop/notes/agrobots/YOLO/data/images'
labels_dir = 'C:/Users/ASUS/Desktop/notes/agrobots/YOLO/data/labels'
train_images_dir = 'C:/Users/ASUS/Desktop/notes/agrobots/YOLO/data/test_images'
train_labels_dir = 'C:/Users/ASUS/Desktop/notes/agrobots/YOLO/data/test'

# Create train directories if they don't exist
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)

# List all files in images directory and shuffle them
all_image_files = os.listdir(images_dir)
shuffle(all_image_files)

# Calculate the split index for 70% of the files
split_idx = int(0.5 * len(all_image_files))

# Move 70% of the images and corresponding labels to the train directories
for image_file in all_image_files[:split_idx]:
    # Derive the corresponding label file name
    label_file = os.path.splitext(image_file)[0] + '.txt'

    # Paths for source files
    image_path = os.path.join(images_dir, image_file)
    label_path = os.path.join(labels_dir, label_file)

    # Paths for destination
    train_image_path = os.path.join(train_images_dir, image_file)
    train_label_path = os.path.join(train_labels_dir, label_file)

    # Move the files
    shutil.move(image_path, train_image_path)
    shutil.move(label_path, train_label_path)

print("Files have been shuffled and moved.")
