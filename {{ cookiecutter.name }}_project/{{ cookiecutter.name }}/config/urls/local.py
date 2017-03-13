from django.conf import settings
from django.conf.urls.static import static

from config.urls.base import *
from core.views import error404


urlpatterns = urlpatterns + [
    url(
        regex=r'^error404/$',
        view=error404,
        name='error404'
    ),
    {% if cookiecutter.use_debug_toolbar -%}
    url(
        regex=r'^__debug__/',
        view=include(debug_toolbar.urls)
    ),
    {%- endif %}
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
