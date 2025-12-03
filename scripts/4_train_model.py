from ultralytics import YOLO


model = YOLO('yolov8s.pt')


model.train(
    data='fruit_yolo_dataset/data.yaml',
    epochs=100,
    imgsz=640,
    batch=8,
    device='mps',
    name='fruit_detector'
)

print("\nTraining complete! Check runs/detect/fruit_detector/")