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
    url(r'^building/(?P<pk>[0-9]+)/$', BuildingDetail.as_view(), name='building-details'),
    url(r'^building/(?P<crimes__year_month>\d{4}-\d{2}-\d{2})/$', BuildingList.as_view(), name='building-month'),
    url(r'^crimes/$', CrimesList.as_view()),
    url(r'^crimes/(?P<pk>[0-9]+)/$', CrimesDetail.as_view(), name='crimes-details'),
    url(r'^api-token-auth/', views.obtain_auth_token),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls
