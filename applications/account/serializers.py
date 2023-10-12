from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.Serializer):
    password_again = serializers.CharField(required=True, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password_again')

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password_again')

        if p1 != p2:
            raise serializers.ValidationError('пароли не совпадают')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
