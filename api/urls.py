from django.urls import include, path
from .views import UserRegistrationView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
]