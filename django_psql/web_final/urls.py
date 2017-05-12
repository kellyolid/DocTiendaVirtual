from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^registrop/$', views.product_register, name='preg'),
    url(r'^search/$', views.search,name='search'),
    url(r'^about/$', views.about, name='about'),
    url(r'^registroc/$', views.categoria_register, name='creg'),
    url(r'^producto/$', views.producto, name='producto'),
    url(r'^searchc/$', views.searchc, name='searchc'),
]