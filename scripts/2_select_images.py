"""
Script 2: Select Images for Annotation Practice
Picks 5 images per fruit (45 total) for you to annotate
"""

import random
import shutil
from pathlib import Path

# ===== CONFIGURATION =====
DATASET_PATH = "dataset"
OUTPUT_PATH = "fruit_annotation_practice"
IMAGES_PER_FRUIT = 5

# Fruit folder names (with spaces as they appear in your dataset)
FRUIT_FOLDERS = [
    'apple fruit',
    'banana fruit', 
    'cherry fruit',
    'chickoo fruit',
    'grapes fruit',
    'kiwi fruit',
    'mango fruit',
    'orange fruit',
    'strawberry fruit'
]

# ===== CREATE OUTPUT FOLDER =====
output_path = Path(OUTPUT_PATH)
output_path.mkdir(exist_ok=True)
print(f"✅ Created folder: {OUTPUT_PATH}")

# ===== SELECT IMAGES =====
print("\n" + "=" * 60)
print("SELECTING IMAGES FOR ANNOTATION")
print("=" * 60)

dataset_path = Path(DATASET_PATH)
total_selected = 0

for fruit_folder in FRUIT_FOLDERS:
    # Get simple fruit name (remove " fruit" part)
    fruit_name = fruit_folder.replace(' fruit', '')
    
    print(f"\n🔍 Selecting {fruit_name} images...")
    
    folder_path = dataset_path / fruit_folder
    
    # Get all images from this folder
    fruit_images = list(folder_path.glob("*.jpg"))
    fruit_images.extend(list(folder_path.glob("*.png")))
    
    if len(fruit_images) == 0:
        print(f"   ⚠️  No images found in {fruit_folder}")
        continue
    
    print(f"   Found {len(fruit_images)} images")
    
    # Select random images
    num_to_select = min(IMAGES_PER_FRUIT, len(fruit_images))
    selected = random.sample(fruit_images, num_to_select)
    
    # Copy with clean naming: apple_001.jpg, apple_002.jpg, etc.
    for i, img in enumerate(selected, 1):
        extension = img.suffix
        new_name = f"{fruit_name}_{i:03d}{extension}"
        destination = output_path / new_name
        
        shutil.copy(img, destination)
    
    print(f"   ✅ Selected {num_to_select} images")
    total_selected += num_to_select

# ===== SUMMARY =====
print("\n" + "=" * 60)
print("SELECTION COMPLETE")
print("=" * 60)

print(f"\n✅ Total images selected: {total_selected}")
print(f"📁 Location: {OUTPUT_PATH}")

print(f"\n📋 NEXT STEPS:")
print(f"1. Open the '{OUTPUT_PATH}' folder")
print(f"2. You'll see {total_selected} images ready for annotation")
print(f"3. Next: Annotate these using Roboflow or LabelImg")

print("\n" + "=" * 60)