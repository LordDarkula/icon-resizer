import click

from icon import __version__
from icon.commands import appicon, tabbar


@click.group(invoke_without_command=True)
@click.pass_context
@click.option('--version', '-v', is_flag=True, help="Show current version")
def main(ctx, version):
    if ctx.invoked_subcommand is None and not version:
        click.echo(ctx.get_help())
    elif version:
        click.echo(__version__)


main.add_command(appicon.appicon)
main.add_command(tabbar.tabbar)
