from PIL import Image, ImageFilter
from pathlib import Path
import os

os.makedirs("filtered2", exist_ok=True)

input_folder = Path("nofilter")
output_folder = Path("filtered2")
filetypes = (".png", ".jpg")

i = 1
for file in input_folder.iterdir():
    if file.suffix.lower() in filetypes:
        photo = Image.open(file)
        filtered = photo.filter(ImageFilter.EMBOSS)
        newname = f"filtered2/{i}_11.2.jpg"
        filtered.save(newname)

        print(f"Размер: {photo.size}")
        print(f"Формат: {photo.format}")
        print(f"Цветовая модель: {photo.mode}\n")
        i += 1