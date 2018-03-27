import os
import click
from typing import List, Tuple, Text
from PIL import Image

from definitions import icon_names, icon_sizes


@click.command()
@click.argument('raw')
@click.option('--output', '-o', default='.', help="Specify output location")
def resize(raw: Text, output):
    if os.path.exists(raw):
        image = Image.open(raw)
        names_and_images = [(name, resize(image, size))
                            for name, size in zip(icon_names, icon_sizes)]
        os.chdir(output)
        os.makedirs('output')
        _save(os.getcwd(), names_and_images)


def _resize(img, size: int):
    return img.resize((size, size), Image.ANTIALIAS)


def _save(destination, names_and_images: List[Tuple[str, Image]]):
    for name, image in names_and_images:
        image.save(os.path.join(destination, name))
