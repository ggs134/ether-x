"""urlconf for the base apuplication"""

from django.conf.urls import url, patterns, include
from . import views

urlpatterns  = [
	url(r'^$', views.home, name='home'),
]
