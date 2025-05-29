import random
from PIL import Image
def databend(img_path, intensity=0.1):
    with open(img_path, "rb") as f:
        data = bytearray(f.read())
   
    # Corrupt random bytes
    for i in range(int(len(data) * intensity)):
        data[random.randint(0, len(data)-1)] = random.randint(0, 255)
   
    with open("sorted_glitch.jpg", "wb") as f:
        f.write(data)
   
    return Image.open("sorted_glitch.jpg")  

