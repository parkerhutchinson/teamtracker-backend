from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from profiles import views

urlpatterns = [
    url(r'^api/profiles/$', views.ProfilesAllAPIView.as_view()),
    # url(r'^api/profiles/(?P<ph>[0-9]+)/$', views.ProfilesAPIView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)