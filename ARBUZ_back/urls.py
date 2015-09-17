"""ARBUZ_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from core.views import BuildingList, CrimesList, BuildingDetail, CrimesDetail
from rest_framework.authtoken import views


router = routers.DefaultRouter()
# router.register(r'building', BuildingList, base_name='building-list')
# router.register(r'crimes', CrimesList)
# router.register(r'building_details', BuildingDetails, base_name='building-details')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^building/$', BuildingList.as_view()),
    # url(r'^crimes/(?P<month>[-\w]+)/building/$', BuildingList.as_view()),
    url(r'^building/(?P<pk>[0-9]+)/$', BuildingDetail.as_view(), name='building-details'),
    url(r'^crimes/$', CrimesList.as_view()),
    url(r'^crimes/(?P<pk>[0-9]+)/$', CrimesDetail.as_view(), name='crimes-details'),
    url(r'^api-token-auth/', views.obtain_auth_token),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls
