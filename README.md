# Fruit Detection with YOLOv8

A machine learning project that detects and classifies 9 types of fruits using YOLOv8 object detection.

## Fruits Detected
- Apple
- Banana
- Cherry
- Chickoo
- Grapes
- Kiwi
- Mango
- Orange
- Strawberry

## Dataset
- Total images: 332
- Annotated for training: 64 images
- Tool used: Roboflow

## Model
- Architecture: YOLOv8 Nano
- Framework: Ultralytics
- Training device: Apple M3 (MPS)
- Epochs: 50

## Project Structure
```
fruit_detection_project/
├── scripts/
│   ├── 1_explore_dataset.py
│   ├── 2_select_images.py
│   ├── 4_train_model.py
│   └── test_custom_image.py
└── runs/detect/fruit_detector/
    └── weights/best.pt
```

## How to Use

### Train the Model
```bash
python3 scripts/4_train_model.py
```

### Test on Custom Image
```bash
python3 scripts/test_custom_image.py
```

## Requirements
```bash
pip install ultralytics opencv-python
```

## Results
Model trained on 64 annotated images with transfer learning from YOLOv8n pretrained weights.


