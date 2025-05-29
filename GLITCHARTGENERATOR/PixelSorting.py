import numpy as np
from PIL import Image

def pixel_sort(img_path, threshold=100):
    img = Image.open(img_path)
    pixels = np.array(img)
   
    # Sort rows by brightness (R+G+B)
    for row in pixels:
        brightness = row.sum(axis=1)
        mask = brightness > threshold  # Only sort bright areas
        row[mask] = np.sort(row[mask], axis=0)
   
    return Image.fromarray(pixels)

# Usage
pixel_sort("y-s-9UN-SXYdcOQ-unsplash.jpg").save("sorted_glitch.jpg")