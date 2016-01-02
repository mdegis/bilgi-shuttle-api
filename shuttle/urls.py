from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from respite.urls import resource, routes, templates
from bilgi.views import PostViews
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin', include(admin.site.urls)),
    url(r'^favicon.ico$', RedirectView.as_view(url='http://www.bilgi.edu.tr/site_media/images/main/favicon.ico', permanent=True), name='some_redirect'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
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
            regex = r'^(?P<campus>[a-zA-Z]+)%s$' % (templates.format),
            view = 'show',
            method = 'GET',
            name = 'post'
        ),
    ]
)
