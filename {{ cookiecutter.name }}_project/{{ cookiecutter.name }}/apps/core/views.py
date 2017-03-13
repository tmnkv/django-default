from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'core/index.html'


def error404(request):
    return render(request, 'core/404.html', status=404)
