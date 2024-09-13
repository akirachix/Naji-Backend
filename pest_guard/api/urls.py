from django.urls import path
from .views import UserListView, UserDetailView, RegisterView, LoginView
from .views import FarmerListView
from .views import FarmerDetailView
from .views import PestListView
from .views import PestDetailView
from .views import Pest_IncidentListView
from .views import Pest_IncidentDetailView
from .views import RecommendListView
from.views import RecommendDetailView


urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user-detail'),
    path('users/register/', RegisterView.as_view(), name='user-register'),
    path('users/login/', LoginView.as_view(), name='user-login'),
     path("farmer/" ,FarmerListView.as_view(),name="farmer_list_view"),
    path("farmer/",FarmerDetailView.as_view(), name="farmer_detail_view"),
    path("pest/" ,PestListView.as_view(),name="pests_list_view"),
    path("pest/" , PestDetailView.as_view(), name="pest_detail_view"),
     path('pestincident/', Pest_IncidentListView.as_view(), name='pest_incident-list'),
    path('pestincident/', Pest_IncidentDetailView.as_view(), name='pest_incident-detail'),
    path('recommendation/', RecommendListView.as_view(), name='recommend-list'),
    path('recommendation/<int:id>/', RecommendDetailView.as_view(), name='recommend-detail'),
]








    
