from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from resources import views

urlpatterns = [
    url(r'^api/resources/$', views.ResourcesAllAPIView.as_view()),
    url(r'^api/resources/(?P<pk>[0-9]+)/$', views.ResourcesAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)