from django.urls import path
from .views import FluxDataAPIView


urlpatterns = [
    path('flux/', FluxDataAPIView.as_view()),
]
