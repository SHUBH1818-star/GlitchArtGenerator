from PIL import Image
import random

def glitch_image(input_path, output_path="glitch_art.jpg"):
    img = Image.open(input_path)
    pixels = img.load()
   
    # Glitch effect: Channel swapping with randomness
    for i in range(img.width):
        for j in range(img.height):
            if random.random() > 0.7:  # 10% corruption rate
                pixels[i, j] = (
                    pixels[i, j][1],  # Swap R and G
                    pixels[i, j][2],  # Swap G and B
                    pixels[i, j][0]   # Swap B and R
                )
    img.save(output_path)
    print(f"Glitch art saved to {output_path}")

# Usage
glitch_image("y-s-9UN-SXYdcOQ-unsplash.jpg")  # Replace with your image path

