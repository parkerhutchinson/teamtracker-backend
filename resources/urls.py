from django.conf.urls import url
from resources import views

urlpatterns = [
    url(r'^api/resources/(?P<pk>[0-9]+)/$', views.ResourceAPIView.as_view()),
]