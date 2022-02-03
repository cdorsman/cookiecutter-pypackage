#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def remove_directory(dirpath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, dirpath))

if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')
    
    if '{{ cookiecutter.command_line_interface }}' != 'y':
        lib_dir = os.path.join('{{ cookiecutter.project_slug }}', 'lib')
        cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')
        remove_file(cli_file)
        remove_directory(lib_dir)

    if '{{ cookiecutter.use_pypi_deployment_with_travis }}' == 'y':
        remove_file('.travis')


    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')
