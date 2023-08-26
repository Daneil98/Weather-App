from django.contrib import admin
from django.urls import path
from View_Weather import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('location/', views.weather_now, name ='location'),
    path('', views.home, name ='index'),
]