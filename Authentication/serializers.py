from rest_auth.registration.serializers import RegisterSerializer
from .models import User

class CustomRegisterSerializer(RegisterSerializer):
    class Meta:
        model = User
        fields = ('email', 'name')