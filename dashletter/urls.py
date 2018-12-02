from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashletter-home'),
    path('about', views.about, name='dashletter-about')
]
