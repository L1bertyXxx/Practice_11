from PIL import Image, ImageFilter
import os
os.makedirs("filtered", exist_ok=True)

for i in range(1, 6):
    filename = f"nofilter/{i}.jpg"
    photo = Image.open(filename)
    newphoto = photo.filter(ImageFilter.GaussianBlur(10))
    name = f"filtered/{i}_11.1.jpg"
    newphoto.save(name)