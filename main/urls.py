from django.conf.urls import patterns, include, url

urlpatterns = patterns('main.views',
    #----------Main----------
    url(r'^$', 'index'),
    #----------Trip----------
    url(r'^trip/$', 'trip'),
    url(r'^trip/(?P<trip_id>\d+)/$', 'trip'),
    #----------Message----------
    url(r'^message/(?P<receiver_id>\d+)/$', 'message'),
    #----------Contact----------
    url(r'^contact/$', 'contact'),
    #----------Python social auth----------
    url('', include('social.apps.django_app.urls', namespace='social')),
    #----------Contact----------
    url(r'^logout/$', 'logout'),
)