import os
import click


@click.command()
@ click.argument('raw')
def resize(raw):
    if os.path.exists(raw):
        pass
