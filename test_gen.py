import unittest
import os
import shutil
import numpy as np
from PIL import Image
from random import seed

from gen import (
    output_dir,
    image_width,
    image_height,
    jpeg_quality,
    noise_generators,
    generate_random_image
)

class TestRandomImageGenerator(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for test outputs
        self.test_dir = "test_output"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        # Clean up the temporary directory after tests
        shutil.rmtree(self.test_dir)

    def test_image_dimensions(self):
        for generator in noise_generators:
            img_array = generator()
            self.assertEqual(img_array.shape, (image_height, image_width, 3),
                             f"Image dimensions incorrect for generator {generator.__name__}")

    def test_image_pixel_values(self):
        for generator in noise_generators:
            img_array = generator()
            self.assertTrue(np.all(img_array >= 0) and np.all(img_array <= 255),
                            f"Pixel values out of bounds in {generator.__name__}")

    def test_random_image_file_creation(self):
        test_path = os.path.join(self.test_dir, "test_image.jpg")
        generate_random_image(test_path)

        # Check file exists
        self.assertTrue(os.path.exists(test_path), "Generated image file does not exist")

        # Check it's a valid image
        with Image.open(test_path) as img:
            self.assertEqual(img.size, (image_width, image_height))
            self.assertEqual(img.format, "JPEG")

    def test_consistent_output_with_seed(self):
        # Optional: test for deterministic output if you decide to use a fixed seed
        seed(42)
        np.random.seed(42)
        img_array_1 = noise_generators[0]()
        seed(42)
        np.random.seed(42)
        img_array_2 = noise_generators[0]()
        self.assertTrue(np.array_equal(img_array_1, img_array_2),
                        "Noise generator does not produce consistent output with fixed seed")

if __name__ == "__main__":
    unittest.main()
