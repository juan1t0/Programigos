from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$',views.index, name="index"),
	url(r'^login/$',views.Login),
	url(r'^logout/$',views.Logout),
	url(r'^registrar/$', views.registrar),
	url(r'^success/$', views.success, name="success"),
	url(r'^preguntar/$',views.preguntar),
	url(r'^about/$',views.acerca),
]