from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import CustomUser

class CustomUserCreationfrom(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'number')

class CustomUserChangefrom(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'number')

