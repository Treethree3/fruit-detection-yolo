"""
Script 1: Explore Your Fruit Dataset
Run this first to understand what you have
"""

import os
from pathlib import Path
from collections import Counter

# ===== CONFIGURATION =====
DATASET_PATH = "./dataset"  # This points to your dataset folder

# ===== EXPLORE STRUCTURE =====
print("=" * 60)
print("EXPLORING DATASET STRUCTURE")
print("=" * 60)

dataset_path = Path(DATASET_PATH)

if not dataset_path.exists():
    print(f"❌ ERROR: Dataset not found at {DATASET_PATH}")
    exit()

# Show folder structure
print("\n📁 Folders found:")
folders = [f.name for f in dataset_path.iterdir() if f.is_dir()]
for folder in sorted(folders):
    print(f"   📂 {folder}")

# Count images in each folder
print("\n📸 Images per fruit:")
total_images = 0

for folder in sorted(folders):
    folder_path = dataset_path / folder
    images = list(folder_path.glob("*.jpg")) + list(folder_path.glob("*.png"))
    print(f"   {folder}: {len(images)} images")
    total_images += len(images)

print(f"\n✅ Total images: {total_images}")

# Show sample paths
print("\n📋 Sample image paths:")
all_images = list(dataset_path.rglob("*.jpg")) + list(dataset_path.rglob("*.png"))
for img in all_images[:5]:
    print(f"   {img.relative_to(dataset_path)}")

print("\n" + "=" * 60)
print("✅ Dataset loaded successfully!")
print("=" * 60)