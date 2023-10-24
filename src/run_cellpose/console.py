import click

@click.command
@click.option(
    '--long', '-s',
    required=True,
    default=1,
    help='help'
)
def main():
