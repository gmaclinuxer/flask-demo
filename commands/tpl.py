# -*- coding: utf-8 -*-
"""
import click
from flask import current_app
from flask.cli import with_appcontext


from common.database import db


@click.command()
@click.option('--file', default='schema.sql',
              help='Sql File To Load (ex. /static/image.png)')
@with_appcontext
def command():
    print '[%s]: <reset db>' % current_app
"""
