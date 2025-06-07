# Random Image Generator

This Python script generates a large dataset of random images for purposes such as machine learning experiments, performance benchmarking, stress testing, or synthetic dataset creation. It outputs JPEG images with randomized patterns and noise until a target disk size is reached.

## Features

* Generates a variety of image patterns:

  * Uniform noise
  * Stripes
  * Checkerboards
  * Gradient noise
  * Random colored blobs
* Applies optional Gaussian blur for visual variation
* Automatically saves images in JPEG format with specified quality
* Progress tracking using `tqdm`
* Configurable output size and image resolution

## Example Use Cases

* Benchmarking image processing pipelines
* Training machine learning models with synthetic data
* Load testing file I/O or image-serving infrastructure
* Evaluating storage requirements for image datasets

## Requirements

* Python 3.7+
* [`numpy`](https://pypi.org/project/numpy/)
* [`Pillow`](https://pypi.org/project/Pillow/)
* [`tqdm`](https://pypi.org/project/tqdm/)

Install dependencies:

```bash
pip install numpy pillow tqdm
```

## Configuration

Edit the following variables at the top of the script to customize behavior:

```python
output_dir = "random_images"   # Output directory
target_size_gb = 64            # Total size of generated images
image_width = 512              # Width of each image
image_height = 512             # Height of each image
jpeg_quality = 85              # JPEG compression quality (1–95)
```

## Running the Script

```bash
python gen.py
```

Progress is displayed in real-time. When done, you'll have a folder filled with randomly generated JPEG images until the target size is met (default: 64 GB).

## Output

* Directory: `random_images/`
* Filenames: zero-padded 10-digit indexes (e.g., `0000000000.jpg`)
* Format: JPEG

## Sample Patterns

Each image is randomly chosen from the following types:

* **Uniform Noise**: Fully random pixels
* **Stripes**: Alternating colored vertical bars
* **Checkerboard**: Alternating color grid
* **Gradient Noise**: Linear gradient + noise
* **Blob Pattern**: Random soft-colored circles

## License

This project is released under the [MIT License](LICENSE), feel free to use and modify it as needed.
