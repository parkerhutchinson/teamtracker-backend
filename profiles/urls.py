from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from profiles import views

urlpatterns = [
    url(r'^profiles/$', views.ProfilesView.as_view()),
]