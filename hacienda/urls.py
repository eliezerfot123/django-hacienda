from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'login.views.home'),
    url(r'^sdr/$', TemplateView.as_view(template_name="index.html")),
    url(r'^$', 'login.views.home', name='home'),
)
