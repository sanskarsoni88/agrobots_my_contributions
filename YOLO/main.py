from ultralytics import YOLO

# Load a model
#model = YOLO("yolov8s.yaml")  # build a new model from scratch
model = YOLO("yolov8s.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="config.yaml", epochs=1)  # train the model
