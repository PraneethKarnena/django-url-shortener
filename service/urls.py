from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),
    path('api/shorten-url/', views.url_shortener_view, name='url_shortener_api'),
]