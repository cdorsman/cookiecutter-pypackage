#!/usr/bin/env python3
"""Console script for {{cookiecutter.project_slug}}."""

from sys import exit
from platform import python_version, machine, system
from os import utime, makedirs
from os.path import exists, dirname, abspath, join

from logging import getLogger
from logging.config import fileConfig

{% if cookiecutter.command_line_interface == 'yes' %}
from lib.parser import Parser
{%- endif %}

{%- if cookiecutter.config_setup == 'yes' %}
from lib.config import config
{%- endif %}

def main():
    """ Main """


if __name__ == '__main__':
    {%- if cookiecutter.command_line_interface == 'yes' %}
    
    parser = Parser()
    cf = config(parser.config_file)
    
    try:
        if exists(parser.default_logfile) is False:
            basedir = dirname(parser.default_logfile)
            if not exists(basedir):
                makedirs(basedir)
            with open(parser.default_logfile, 'a'):
                utime(parser.default_logfile, None)
    except OSError as oserr:
        print('Cannot open file:', parser.default_logfile)
        exit(1)
    {%- endif %}

    {%- if cookiecutter.command_line_interface == 'yes' %}
    __loggername__ = parser.app_name.title()
    fileConfig(fname=parser.default_logconf)
    {%- else %}
    __loggername__ = "{{cookiecutter.project_slug}}"
    fileConfig(fname={}).format(
        join(
            dirname(dirname(abspath(__file__))),
            'conf')
    )
    {%- endif %}
    log = getLogger(__loggername__)
    log.debug('%s-%s running on Python version: %s-%s on %s',
        __loggername__,
        '{{ cookiecutter.version }}',
        python_version(),
        machine(),
        system())
    log.debug('Configuration settings:\n\n \
Approot: %s |\n \
Logconfig file: %s |\n \
Config file: %s |\n',
                  parser.app_root,
                  parser.default_logconf,
                  parser.config_file)

    main()
