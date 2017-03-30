from django.conf.urls import url, include
from main.views import *

urlpatterns = [
  url(r'^', IndexView.as_view())
]