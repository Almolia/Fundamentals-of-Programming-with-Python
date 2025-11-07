import os
from PIL import Image

# مسیر پوشه عکس‌ها
folder = "."   # اینجا مسیر پوشه را بگذار

# فرمت‌های قابل قبول
valid_ext = (".jpg", ".jpeg", ".png")

for file in os.listdir(folder):
    if file.lower().endswith(valid_ext):
        full_path = os.path.join(folder, file)
        filename, _ = os.path.splitext(file)
        output_path = os.path.join(folder, filename + ".png")

        # اگر خودش PNG بود، رد کن
        if file.lower().endswith(".png"):
            continue

        try:
            img = Image.open(full_path).convert("RGB")
            img.save(output_path, "PNG")
            print(f"Converted: {file} -> {filename}.png")
        except Exception as e:
            print(f"Error converting {file}: {e}")