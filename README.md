# agrobots_my_contributions
Agrobots is a UBC student engineering design team that builds autonomous robots for agricultural use. As a part of the applied AI team, I am training a model to identify maize plants. This model will be used to get relative coordinates of the plants, following which appropriate chemical treatment will be used.

## Dataset collection
After finding annotated datasets for maize plant from the internet, several perprocessing steps were performed such as augmentation, padding, resizing amd crop the images and transform the provided xml annotations too. These files can be found under python_scripts_to_clean_dataset.

## Models
Initially, to get a baseline performance, a YOlOv8 model was trained to give an mAP50 score of 0.63. Here are the inferences made by the model for some of the test images:
![Alt text](/YOLO/runs/detect/train2/val_batch0_labels.jpg)
There are lots of overlapping predictions, non max suppression needs to be strengthened to reduce redundancy. This model was also only trained for 1 epoch on my local machine. Currently I am training Single Shot Detection (SSD) model on a hyper-computing cluster (HPC) to speed up the process. After this, I will try a Masked R-CNN model and compare the accuracy and latency of the models.
