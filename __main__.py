from argparse import ArgumentParser, RawDescriptionHelpFormatter
import click
from collections import namedtuple, OrderedDict
import importlib
from os.path import dirname, isfile, split, splitext
import sys
import textwrap

@click.group()
def main():
	pass

@main.command()
@click.option('--out', type=str, required=False)
@click.option('--normal', type=float, nargs=3, required=False)
@click.option('--base', type=float, nargs3, required=False)
@click.option('--auto/--no-auto', default=False)
@@click.argument('filenames', type=str, nargs=1)

@main.command()
