from django.urls import path, include
from . import views
# from django.views.generic import TemplateView



urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]
