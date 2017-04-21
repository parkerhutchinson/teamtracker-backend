from django.contrib import admin
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^/$', include('main.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include_docs_urls(title='PRPL API')),
]
