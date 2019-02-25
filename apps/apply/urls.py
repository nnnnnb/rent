from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^ajax_region_block_linkage/(?P<region_id>\d+)$', views.ajax_region_block_linkage),
    url(r'^$', views.index, name='index'),
    url(r'index/$', views.index, name='index'),
    url(r'entire/$', views.entire, name='entire'),
    url(r'entiretext/$', views.entiretext, name='entiretext'),
    url(r'life/$', views.life, name='life'),
    url(r'lifetext/$', views.lifetext, name='lifetext'),
    url(r'maps/$', views.maps, name='maps'),
    url(r'ajaxmap/', views.ajaxmap),  
]
