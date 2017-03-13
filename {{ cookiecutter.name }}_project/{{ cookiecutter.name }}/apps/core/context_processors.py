from django.db.models import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned

from apps.core.models import Page, Header, Footer


def add_page(request):
    try:
        page = Page.objects.get(uri=request.path)
    except ObjectDoesNotExist:
        return {'page': None}
    except MultipleObjectsReturned:
        page = Page.objects.filter(uri=request.path)[0]
    breadcrumbs = page.get_ancestors(include_self=True)
    context = dict()
    context['page'] = page
    context['breadcrumbs'] = breadcrumbs
    if page.text_block_list:
        for block in page.text_block_list.all():
            context[block.placeholder] = block.text
    return context


def add_header(request):
    try:
        header = Header.objects.filter(mptt_level=0).prefetch_related(
            'page',
            'header_child__page'
        )
    except ObjectDoesNotExist:
        header = None
    return {'header': header}


def add_footer(request):
    try:
        footer = Footer.objects.filter(mptt_level=0).prefetch_related(
            'page',
            'footer_child__page'
        )
    except ObjectDoesNotExist:
        return {'footer': None}
    return {
        'footer': footer,
            }
