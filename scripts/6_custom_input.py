
from ultralytics import YOLO
from tkinter import Tk, filedialog

model = YOLO('runs/detect/fruit_detector/weights/best.pt')

root = Tk()
root.withdraw()

test_image = filedialog.askopenfilename(
    filetypes=[("Images", "*.jpg *.jpeg *.png")]
)

if test_image:
    results = model(test_image)
    results[0].show()

root.destroy()