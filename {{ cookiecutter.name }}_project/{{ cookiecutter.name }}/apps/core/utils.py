import re
from uuid import uuid4

from django.core.validators import RegexValidator

IMG = 'images/'
VIDEO = 'videos/'
DOC = 'documents/'
OTHER = 'other/'

phone_regex = RegexValidator(
    regex=r'(8|\+7)(\s|\-)?(\d{3}|\(\d{3}\))(\s|\-)?\d{3}(\s|\-)?\d{2}(\s|\-)?\d{2}',
    message='Формат ввода: +79012346767'
)


def search(pattern, filename):
    if re.search(pattern, filename):
        return True
    else:
        return False


def is_image(filename):
    pattern = '.+\.(jpg|png|jpeg|gif)(?iu)'
    return search(pattern, filename)


def is_video(filename):
    pattern = '.+\.(mp4|avi|mkv|mov)(?iu)'
    return search(pattern, filename)


def is_document(filename):
    pattern = '.+\.(pdf|doc|docx|xls|xlsx)(?iu)'
    return search(pattern, filename)


def rename(filename):
    ext = filename.split('.')[-1]
    hash = uuid4().hex
    return '{}/{}/{}.{}'.format(hash[:2], hash[2:4], hash, ext)

def upload(instance, filename):
    if is_image(filename):
        return '{}{}'.format(IMG, rename(filename))
    elif is_video(filename):
        return '{}{}'.format(VIDEO, filename)
    elif is_document(filename):
        return '{}{}'.format(DOC, filename)
    else:
        return '{}{}'.format(OTHER, rename(filename))