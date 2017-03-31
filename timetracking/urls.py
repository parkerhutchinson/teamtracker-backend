from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from timetracking import views

urlpatterns = [
    url(r'^api/tracker/$', views.TimeTrackingAPIView.as_view()),
    url(r'^api/tracker/(?P<pk>[0-9]+)/$', views.TimeTrackingAPIView.as_view()),
    url(r'^api/what/$', views.What.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)