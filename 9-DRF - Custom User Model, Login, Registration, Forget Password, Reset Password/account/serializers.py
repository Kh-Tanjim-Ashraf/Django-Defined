from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings



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



class UserPasswordUpdateSerializer(serializers.ModelSerializer):

    old_password = serializers.CharField(max_length=255)
    password1 = serializers.CharField(max_length=255)
    password2 = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['old_password', 'password1', 'password2']
    
    def validate(self, attrs):
        old_password = attrs.get('old_password')
        password1 = attrs.get('password1')
        password2 = attrs.get('password2')
        user = self.context.get('user')

        # Cross-check old password
        if not user.check_password(old_password):
            raise serializers.ValidationError("Invalid current pasword")

        if password1 != password2:
            raise serializers.ValidationError("The two passwords didn't match")
        
        user.set_password(password1)
        user.save()
        
        return attrs



class UserForgetPassowrdSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length=255)

    def validate(self, attrs):
        if not User.objects.filter(email=attrs.get('email')).exists():
            raise serializers.ValidationError("No account is associated with this email address")

        user = User.objects.get(email=attrs.get('email'))

        # Build the magic password reset link
        uid = urlsafe_base64_encode(force_bytes(user.id))
        token = default_token_generator.make_token(user)
        link = f"{settings.FRONTEND_URL}/reset-password/{uid}/{token}"
        
        # TODO: Send email to user's mailbox
        print("magic link:", link)

        return attrs