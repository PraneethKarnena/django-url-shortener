from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),
    path('api/shorten-url/', views.url_shortener_api, name='url_shortener_api'),
    path('api/shorten-url', views.url_shortener_api, name='url_shortener_api_safe'),
    path('l/<slug:slug>/', views.redirector_view),
]