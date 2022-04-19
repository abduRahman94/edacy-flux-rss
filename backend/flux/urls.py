from django.urls import path
from .views import get_flux


urlpatterns = [
    path('', get_flux)
]