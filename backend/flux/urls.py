from django.urls import path
from .views import FluxDataAPIView


urlpatterns = [
    path('', FluxDataAPIView.as_view())
]