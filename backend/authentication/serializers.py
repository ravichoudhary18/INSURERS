from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if password is None:
            raise serializers.ValidationError('A password is required to login.')

        if '@' in username:
            try:
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                raise serializers.ValidationError({'error': 'This email address is not associated with any account.'})

            if not user.check_password(password):
                raise serializers.ValidationError({'error' : 'Invalid username or password.'})
        else:
            user = authenticate(username=username, password=password)

            if user is None:
                raise serializers.ValidationError({'error' : 'Invalid username or password.'})

        if not user.is_active:
            raise serializers.ValidationError({'error' : 'This user account is not active.'})

        return {'user': user}

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class UserInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'created_at', 'created_by', 'last_login']