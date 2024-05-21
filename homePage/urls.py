from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),  # This pattern will match the root URL
    path('about/', views.about, name = 'about'),
]
