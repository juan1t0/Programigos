from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^pregunta/$',views.Preguntation),
	url(r'^preguntas/(?P<pregunta_id>\d+)/$',views.detalle, name="detalle"),
]