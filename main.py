import os
from PIL import Image
from pathlib import Path

# 入出力パス設定
filename = input(str("リサイズする画像のファイル名（拡張子も含める）: "))
filename_without_ext = Path(filename).stem
input_path = f"input/{filename}"
output_path = "output"

# 画像サイズを設定
sizes = [192, 512]

def resize_image(input_path, output_path, sizes):
    os.makedirs(output_path, exist_ok=True)

    img = Image.open(input_path)
    for size in sizes:
        resized_img = img.resize((size, size), Image.Resampling.LANCZOS)
        resized_img.save(f"{output_path}/{filename_without_ext}_{size}x{size}.png")
        # 出力ファイル名
        print(f"Saved: {filename_without_ext}_{size}x{size}.png")

resize_image(input_path, output_path, sizes)