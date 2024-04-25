# urls.py within the pages app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),  # Add this line for portfolio
    path('contact/', views.contact, name='contact'),
    # Other URL patterns
]
