from rest_framework import serializers

from api.models import User,Post,Comment

class UserRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    avatar = serializers.ImageField(write_only=True,allow_empty_file=True,use_url=True)
    biography = serializers.CharField(write_only=True)

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        avatar = validated_data.pop('avatar')
        biography = validated_data.pop('biography')

        user = User.objects.create_user(username,None,password,**validated_data)
        user.avatar = avatar
        user.biography = biography
        return user

    class Meta:
        model = User
        fields = ['username','password','avatar','biography']
