from django.urls import path
from django.contrib import admin
from .views import PestIncidentListView, PestIncidentDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pest-incident/', PestIncidentListView.as_view(), name='pest-incident-list'),
    path('pest-incident/', PestIncidentDetailView.as_view(), name='pest-incident-detail'),
]


