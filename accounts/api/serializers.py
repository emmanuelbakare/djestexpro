from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.models import Profile

class ProfileSerializer(serializers.ModelSerializer):

    profile_pic=serializers.ImageField(use_url=True, max_length=None)
    class Meta:
        model = Profile
        fields = ('phone','profile_pic', )

class AccountSerializer(serializers.ModelSerializer):
    profile=ProfileSerializer(read_only=True, many=False)

    class Meta:
        model= get_user_model()
        fields=('id','email','username','profile', 'first_name', 'last_name')
        