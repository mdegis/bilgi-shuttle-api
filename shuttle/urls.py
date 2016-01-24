from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from respite.urls import resource, routes, templates
from shuttle.views import PostViews
from django.views.generic import RedirectView
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls))
]

urlpatterns += resource(
    views = PostViews,
    routes = [
        routes.route(
            regex = r'^(?:$|index%s$)' % (templates.format),
            view = 'index',
            method = 'GET',
            name = 'main'
        ),
        routes.route(
            regex = r'^upload%s$' % (templates.format),
            view = 'upload',
            method = 'GET',
            name = 'upload'
        ),
        routes.route(
            regex = r'^upload%s$' % (templates.format),
            view = 'process_file',
            method = 'POST',
            name = 'process_file'
        ),
        routes.route(
            regex = r'^(?P<campus>[a-zA-Z]+)%s$' % (templates.format),
            view = 'show',
            method = 'GET',
            name = 'post'
        ),
    ]
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)