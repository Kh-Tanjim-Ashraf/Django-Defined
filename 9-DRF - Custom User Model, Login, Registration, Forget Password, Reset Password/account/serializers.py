from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):

    # Since `password2` is not a field of `User` model, we are required to explicitly define this field here
    password2 = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'username', 'password', 'password2']
    
    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError("The two passwords didn't match")

        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')

        return User.objects.create_user(**validated_data)



class UserLoginSerializer(serializers.ModelSerializer):

    # Since the `email` field of `User` model raises unique email error if an already existing email is passed from the client, thus an `email` field is explicitly defined here
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'password']



class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'is_active', 'is_superuser']