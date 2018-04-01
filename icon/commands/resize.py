import os
import click
from typing import List, Tuple, Dict, Text
from PIL import Image

from definitions import icon_dict


@click.command()
@click.argument('raw')
@click.option('--output', '-o', default='.', help="Specify output location")
@click.option('--tab-bar', '-b', is_flag=True, help="Show current version")
def resize(raw, output):
    """ Resize icon to Apple's required sizes and save them to current directory. """
    if os.path.exists(raw):
        image = Image.open(raw)
        names_and_images = dict([(name, resize(image, size))
                                 for name, size in icon_dict.items()])
        os.chdir(output)
        os.makedirs('output')
        _save(os.getcwd(), names_and_images)


def _resize(img, size: int):
    return img.resize((size, size), Image.ANTIALIAS)


def _save(destination, image_dict: Dict):
    for name, image in image_dict.items():
        image.save(os.path.join(destination, name))
