import os
import click
from typing import Dict
from PIL import Image

import definitions


@click.group(invoke_without_command=True)
@click.pass_context
@click.option('--version', '-v', is_flag=True, help="Show current version")
def tabbar(ctx, version: bool):
    """ Manipulate raw tab bar glyph """
    if ctx.invoked_subcommand is None and not version:
        click.echo(ctx.get_help())


@tabbar.command()
@click.argument('raw')
@click.option('--output', '-o', default=None, help="Specify output location")
def resize(raw, output: str):
    """ Resize icon to Apple's required sizes """
    output = output or os.getcwd()
    if os.path.exists(raw):
        image = Image.open(raw)
        resized_dict = {name: image.resize((size, size), Image.ANTIALIAS)
                        for name, size in definitions.tab_bar_dict.items()}
        os.chdir(os.path.abspath(output))
        os.makedirs('output')
        _save(os.getcwd(), resized_dict)
    else:
        click.echo("No image file found at {}. Please specify valid glyph path.".format(raw))


def _save(destination: str, image_dict: Dict):
    for name, image in image_dict.items():
        image.save(os.path.join(destination, name))
