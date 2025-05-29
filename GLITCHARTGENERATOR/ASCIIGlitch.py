from PIL import Image
import random
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
def ascii_glitch(img_path, width=100):
    img = Image.open(img_path).convert("L")  # Grayscale
    img = img.resize((width, int(width * img.height / img.width)))
   
    ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    pixels = img.getdata()
   
    # Corrupt every 10th character
    corrupted = [
        ascii_chars[min(pixel // 25, len(ascii_chars)-1)] if random.random() > 0.1 else "±"
        for pixel in pixels
    ]
   
    return "\n".join("".join(row) for row in chunks(corrupted, width))
result = ascii_glitch("y-s-9UN-SXYdcOQ-unsplash.jpg")  
with open("ascii_glitch.txt", "w") as f:
    f.write(result)