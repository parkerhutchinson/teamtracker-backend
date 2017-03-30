from django.conf.urls import urls
from rest_framework.urlpatterns import format_suffix_patterns
from timetracking import views

urlpatterns = [
    urls(r'^api/tracker/$', views.TimeTrackingAPI.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)