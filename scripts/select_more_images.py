import random
import shutil
from pathlib import Path

dataset_path = Path('dataset')
output_path = Path('fruit_annotation_practice')

fruit_folders = list(dataset_path.iterdir())

for folder in fruit_folders:
    if folder.is_dir():
        images = list(folder.glob("*.jpg")) + list(folder.glob("*.png"))
        
        # Pick 3 more random images from each fruit
        selected = random.sample(images, min(3, len(images)))
        
        for img in selected:
            shutil.copy(img, output_path / img.name)

print("✅ Added more images to annotation folder!")