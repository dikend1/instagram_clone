from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from api.models import User
from api.seriailzers import UserRegistrationSerializer


# Create your views here.

class UserRegistrationView(CreateAPIView):
    model = User
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer
