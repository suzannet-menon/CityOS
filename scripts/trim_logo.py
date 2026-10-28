import sys
from PIL import Image

src = Image.open(r"D:\CityOS\mobile\assets\civix_logo.png").convert("RGBA")
bbox = src.getchannel("A").getbbox()
print("orig", src.size, "bbox", bbox)
trimmed = src.crop(bbox)
trimmed.save(r"D:\CityOS\mobile\assets\civix_logo.png")
print("trimmed to", trimmed.size)

icon = Image.open(r"D:\CityOS\mobile\assets\logo_icon.png").convert("RGBA")
icon.resize((64, 64), Image.LANCZOS).save(r"D:\CityOS\mobile\web\favicon.png")
print("favicon 64x64 written")
