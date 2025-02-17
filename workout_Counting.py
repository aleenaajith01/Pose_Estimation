import cv2
from ultralytics import YOLO, solutions

model = YOLO("yolov8n-pose.pt")
cap = cv2.VideoCapture(r"C:\Users\Aleena Ajith\OneDrive\Desktop\YOLO\Action_detection\8027449-uhd_4096_2160_25fps.mp4")
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

video_writer = cv2.VideoWriter("squat2.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

gym_object = solutions.AIGym(
    line_thickness=2,
    view_img=True,
    pose_type="squat",
    kpts_to_check=[6, 8, 10],
)

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break
    results = model.track(im0, verbose=False)  # Tracking recommended
    #results = model.predict(im0)  # Prediction also supported
    im0 = gym_object.start_counting(im0, results)

    video_writer.write(im0)

cv2.destroyAllWindows()
video_writer.release()