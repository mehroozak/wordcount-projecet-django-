

from django.urls import path

from . import views


urlpatterns = [
	path('', views.home, name= 'home'),
	path('counter/', views.count, name='count'),
	path('about-us', views.about, name= 'about'),
]
