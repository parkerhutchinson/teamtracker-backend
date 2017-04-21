from django.conf.urls import url, include
from main.views import *

urlpatterns = [
    url(r'^', include('profiles.urls')),
    url(r'^', include('timetracking.urls')),
    url(r'^', include('resources.urls')),
    url(r'^$', IndexView.as_view()),
]
