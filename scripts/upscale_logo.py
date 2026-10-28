from PIL import Image, ImageFilter

p = r"D:\CityOS\mobile\assets\civix_logo.png"
img = Image.open(p).convert("RGBA")
w, h = img.size
up = img.resize((w * 2, h * 2), Image.LANCZOS)
up = up.filter(ImageFilter.UnsharpMask(radius=2, percent=120, threshold=2))
up.save(p)
print("civix_logo ->", up.size)
