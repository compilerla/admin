import click

from compiler_admin.commands.time.convert import convert
from compiler_admin.commands.time.download import download


@click.group
def time():
    """
    Work with Compiler time entries.
    """
    pass


time.add_command(convert)
time.add_command(download)
