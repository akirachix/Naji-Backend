from django.shortcuts import render

# Create your views here.
from recommend.models import Recommend
from .serializers import RecommendSerializer
import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.views import APIView
from pestincident.models import PestIncident
from .serializers import Pest_IncidentSerializer
from farmer.models import Farmer
from .serializers import FarmerSerializer
from rest_framework.response import Response
from pest.models import Pest
from .serializers import PestSerializer
from pest.models import Pest
from rest_framework import status
from user.models import User
from .serializers import UserSerializer, RoleSerializer
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
logger = logging.getLogger(__name__)
class UserListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        logger.info("Retrieved user list.")
        return Response(serializer.data, status=status.HTTP_200_OK)
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            logger.error(f'User with ID {id} not found.')
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        logger.info(f'User with ID {id} retrieved successfully.')
        return Response(serializer.data)
    
class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            logger.info(f'User registered successfully: {user.email}')
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        logger.error(f'User registration failed: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
logger = logging.getLogger(__name__)
User = get_user_model()

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            logger.info(f'Login attempt for non-existent user: {email}')
            return Response({
                'error': 'User does not exist',
                'signup_required': True
            }, status=status.HTTP_404_NOT_FOUND)
        django_user = authenticate(username=email, password=password)
        if django_user:
            logger.info(f'User logged in successfully: {email}')
            return Response({}, status=status.HTTP_200_OK)
        logger.error(f'Login failed for user: {email}')
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class FarmerListView(APIView):
    def get(self, request):
        farmer = Farmer.objects.all()
        serializer = FarmerSerializer(farmer, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = FarmerSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
class FarmerDetailView(APIView):
    def get(self,request,id):
        farmer = Farmer.objects.get(id=id)
        serializer = FarmerSerializer(farmer)
        return Response(serializer.data)

    def put(self, request, id):
        farmer = Farmer.objects.get(id=id)
        serializer = FarmerSerializer(farmer, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, data=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     

  
        
class PestListView(APIView):
    def get(self, request):
        farmer = Farmer.objects.all()
        serializer = FarmerSerializer(farmer, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = FarmerSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
class PestDetailView(APIView):
    def get(self,request,id):
        pest = Pest.objects.get(id=id)
        serializer = PestSerializer(pest)
        return Response(serializer.data)
    


    def post(self, request):
        serializer = Pest_IncidentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        


 



class Pest_IncidentDetailView(APIView):
    def get(self, request, id):
        try:
            pest_incident = PestIncident.objects.get(id=id)
        except pest_incident.DoesNotExist:
            return Response({'error': 'Pest not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = Pest_IncidentSerializer(pest_incident)
        return Response(serializer.data)
   
   
class Pest_IncidentListView(APIView):
    def get(self, request):
        pest_incident = PestIncident.objects.all()
        serializer = Pest_IncidentSerializer(pest_incident, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Pest_IncidentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










class RecommendDetailView(APIView):
    def get(self, request, id):
        try:
            recommend = Recommend.objects.get(id=id)
        except Recommend.DoesNotExist:
            return Response({'error': 'Recommendation not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = RecommendSerializer(recommend)
        return Response(serializer.data)


    def put(self, request, id):
        try:
            recommend = Recommend.objects.get(id=id)
        except Recommend.DoesNotExist:
            return Response({'error': 'Recommendation not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = RecommendSerializer(recommend, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  


class RecommendListView(APIView):
    def get(self, request):
        recommend = Recommend.objects.all()
        serializer = RecommendSerializer(recommend, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecommendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


