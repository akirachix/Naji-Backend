from django.urls import path
from .views import PestIncidentListView, PestIncidentDetailView

urlpatterns = [
    path('pest-incident/', PestIncidentListView.as_view(), name='pest-incident-list'),
    path('pest-incident/', PestIncidentDetailView.as_view(), name='pest-incident-detail'),
]