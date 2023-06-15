from django.urls import path
from .views import ScenarioListCreateView, ScenarioRetrieveView

urlpatterns = [
    path('scenarios/', ScenarioListCreateView.as_view(), name='scenario-list'),
    path('scenarios/<int:pk>/', ScenarioRetrieveView.as_view(), name='scenario-detail'),
]
