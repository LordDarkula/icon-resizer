import os
import click
from PIL import Image

import definitions
from icon.commands import helpers


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
    """ Resize glyph to Apple's required sizes """
    output = output or os.getcwd()
    if os.path.exists(raw):
        image = Image.open(raw)
        resized_dict = {name: image.resize((size, size), Image.ANTIALIAS)
                        for name, size in definitions.tab_bar_dict.items()}
        os.chdir(os.path.abspath(output))
        os.makedirs('output')
        helpers.save_images(os.getcwd(), resized_dict)
    else:
        click.echo("No image file found at {}. Please specify valid glyph path.".format(raw))

