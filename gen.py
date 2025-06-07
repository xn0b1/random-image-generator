import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import os
import random
from tqdm import tqdm

# Configuration pip install numpy pillow tqdm
output_dir = "random_images"
target_size_gb = 64
image_width = 512
image_height = 512
jpeg_quality = 85

target_size_bytes = target_size_gb * 1024**3
os.makedirs(output_dir, exist_ok=True)

def get_file_size(path):
    return os.path.getsize(path)

def generate_uniform_noise():
    return np.random.randint(0, 256, (image_height, image_width, 3), dtype=np.uint8)

def generate_stripes():
    img = np.zeros((image_height, image_width, 3), dtype=np.uint8)
    stripe_width = random.randint(5, 20)
    color1 = np.random.randint(0, 256, (3,))
    color2 = np.random.randint(0, 256, (3,))
    for i in range(0, image_width, stripe_width * 2):
        img[:, i:i+stripe_width] = color1
        img[:, i+stripe_width:i+2*stripe_width] = color2
    return img

def generate_checkerboard():
    img = np.zeros((image_height, image_width, 3), dtype=np.uint8)
    block_size = random.randint(16, 64)
    color1 = np.random.randint(0, 256, (3,))
    color2 = np.random.randint(0, 256, (3,))
    for y in range(0, image_height, block_size):
        for x in range(0, image_width, block_size):
            if (x // block_size + y // block_size) % 2 == 0:
                img[y:y+block_size, x:x+block_size] = color1
            else:
                img[y:y+block_size, x:x+block_size] = color2
    return img

def generate_gradient_noise():
    base = np.tile(np.linspace(0, 255, image_width, dtype=np.uint8), (image_height, 1))
    channel = np.stack([base]*3, axis=2)
    noise = np.random.randint(0, 50, (image_height, image_width, 3), dtype=np.uint8)
    return np.clip(channel + noise, 0, 255).astype(np.uint8)

def generate_blob_pattern():
    img = Image.new('RGB', (image_width, image_height), 'black')
    draw = ImageDraw.Draw(img)
    for _ in range(random.randint(5, 20)):
        radius = random.randint(10, 50)
        x = random.randint(0, image_width)
        y = random.randint(0, image_height)
        color = tuple(np.random.randint(0, 256, (3,)))
        draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=color)
    return np.array(img)

# Random noise generator
noise_generators = [
    generate_uniform_noise,
    generate_stripes,
    generate_checkerboard,
    generate_gradient_noise,
    generate_blob_pattern
]

def generate_random_image(path):
    noise_func = random.choice(noise_generators)
    data = noise_func()
    img = Image.fromarray(data, 'RGB')
    img = img.filter(ImageFilter.GaussianBlur(radius=random.uniform(0, 1.5)))  # optional: softens patterns
    img.save(path, 'JPEG', quality=jpeg_quality)

# Main loop
total_size = 0
image_count = 0

with tqdm(total=target_size_bytes, unit="B", unit_scale=True, desc="Generating Images") as pbar:
    while total_size < target_size_bytes:
        filename = f"{image_count:010}.jpg"
        filepath = os.path.join(output_dir, filename)
        generate_random_image(filepath)
        file_size = get_file_size(filepath)
        total_size += file_size
        pbar.update(file_size)
        image_count += 1

print(f"Done! Generated {image_count} images totaling ~{total_size / (1024**3):.2f} GB")
