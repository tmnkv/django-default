import os

PROJECT_DIR = os.path.realpath(os.path.curdir)
PROJECT_NAME = '{{ cookiecutter.name }}'.lower()


def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)


def remove_jet_settings():
    jet_settings = os.path.join(
        PROJECT_DIR,
        '/'.join([PROJECT_NAME, 'config/settings/jet.py'])
    )
    remove_file(jet_settings)


def remove_behaviors():
    behaviors = os.path.join(
        PROJECT_DIR,
        '/'.join([PROJECT_NAME, 'apps/core/behaviors.py'])
    )
    remove_file(behaviors)


def remove_common_models():
    common_models = os.path.join(
        PROJECT_DIR,
        '/'.join([PROJECT_NAME, 'apps/core/common_models.py'])
    )
    remove_file(common_models)


def remove_context_processor():
    context_processor = os.path.join(
        PROJECT_DIR,
        '/'.join([PROJECT_NAME, 'apps/core/context_processors.py'])
    )
    remove_file(context_processor)


if '{{ cookiecutter.use_jet_admin}}'.lower() != 'y':
    remove_jet_settings()

if '{{ cookiecutter.use_behaviors}}'.lower() != 'y':
    remove_behaviors()

if '{{ cookiecutter.use_common_models}}'.lower() != 'y':
    remove_common_models()

if '{{ cookiecutter.use_mptt }}'.lower() != 'y':
    remove_context_processor()
