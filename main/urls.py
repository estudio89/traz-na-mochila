from django.conf.urls import patterns, include, url

urlpatterns = patterns('main.views',
    #----------Main----------
    url(r'^$', 'index'),
)