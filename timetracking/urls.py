from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from timetracking import views

urlpatterns = [
    url(r'^api/tracker/(?P<pk>[0-9]+)/$', views.TimeTrackingAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)