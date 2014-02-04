from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^liquidaciones/(\d+)/$', 'contribuyentes.views.contrib_liquids', name="contrib-liquids"),
)
