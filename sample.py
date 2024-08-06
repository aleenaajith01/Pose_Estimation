from ultralytics import YOLO

# Load a model
#model = YOLO("yolov8n-pose.pt")  # load an official model
model = YOLO(r"C:\Users\Aleena Ajith\OneDrive\Desktop\YOLO\Pose_Estimation\best.pt")  # load a custom model

# Predict with the model
results = model(r"C:\Users\Aleena Ajith\OneDrive\Desktop\YOLO\Pose_Estimation\cycling.mp4", 
                show=True, conf=0.3, save=True, show_boxes=False)  # predict on an image