from django.conf.urls import include, url
from django.contrib import admin

from packetstore import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'scapjo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^packet_details/(?P<id>\d+)/', views.packet_details, name='packet_details'),
    url(r'^admin/', include(admin.site.urls)),
]
