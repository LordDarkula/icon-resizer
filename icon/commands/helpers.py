import os
from typing import Dict


def save_images(destination: str, image_dict: Dict):
    for name, image in image_dict.items():
        image.save(os.path.join(destination, name))
