import os
from PIL import Image

# 入出力パス設定
input_path = "input/ChatGPT-Image.png"
output_path = "output"
sizes = [192, 512]

def resize_image(input_path, output_path, sizes):
    os.makedirs(output_path, exist_ok=True)

    img = Image.open(input_path)
    for size in sizes:
        resized_img = img.resize((size, size), Image.Resampling.LANCZOS)
        resized_img.save(f"{output_path}/app_icon_{size}x{size}.png")
        # 出力ファイル名
        print(f"Saved: icon_{size}x{size}.png")

resize_image(input_path, output_path, sizes)