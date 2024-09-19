from rest_framework import serializers
from pestincident.models import PestIncident
from farmer.models import Farmer
from pest .models import Pest
from user .models import User 
from django.contrib.auth.models import User as DjangoUser
from recommend.models import Recommend 

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password']
        read_only_fields = ['id']
    def create(self, validated_data):
        django_user = DjangoUser.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user = User.objects.create(
            user=django_user,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            
        )
        return user
class RoleSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    # role = serializers.ChoiceField(choices=User.ROLE_CHOICES)

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = "__all__"

class PestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pest
        fields = "__all__"


class Pest_IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PestIncident
        fields = "__all__"

class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommend
        fields = '__all__'