from ultralytics import YOLO
import random
from pathlib import Path
model = YOLO('runs/detect/fruit_detector/weights/best.pt')
dataset_path = Path('dataset')
fruit_folders = list(dataset_path.iterdir())

test_images = []
for folder in fruit_folders[:3]:
    if folder.is_dir():
        images = list(folder.glob("*.jpg")) + list(folder.glob("*.png"))
        if images:
            test_images.append(random.choice(images))

# Run detection
for img_path in test_images:
    results = model(img_path)
    results[0].show()