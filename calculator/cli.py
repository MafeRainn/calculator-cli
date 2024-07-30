import click

from calculator.model import Calculator

@click.group()
@click.pass_context
def calc(ctx: click.Context):
    """A somple calculator"""
    
    ctx.obj = {"calculator_object", Calculator()}