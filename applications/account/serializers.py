from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from applications.account.tasks import celery_send_activation_code

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password_again = serializers.CharField(required=True, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password_again')

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password_again')

        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        celery_send_activation_code.delay(user.email, user.code)
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=8)
    new_password_confirm = serializers.CharField(required=True, min_length=8)

    def validate_old_password(self, password):
        request = self.context.get('request')
        user = request.user
        if not user.check_password(password):
            raise serializers.ValidationError('Старый пароль неверный!')
        return password

    def validate(self, attrs):
        p1 = attrs.get('new_password')
        p2 = attrs.get('new_password_confirm')

        if p1 != p2:
            raise serializers.ValidationError('Данные пароли не совпадают!')
        return attrs

    def set_new_password(self, new_password):
        request = self.context.get('request')
        user = request.user
        password = self._validated_data.get('new_password')
        user.set_password(password)
        user.save(update_fields=('password'))


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def send_code(self):
        user = get_object_or_404(User, email=self.validated_data.get('email'))
        user.create_activation_code()
        celery_send_activation_code.delay(user.email, user.code)


class ForgotPasswordConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    code = serializers.CharField(required=True)
    new_password = serializers.CharField(min_length=8, required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        code = attrs.get('code')
        user = get_object_or_404(User, email=email, code=code)
        attrs['user'] = user
        return attrs

    def set_new_password(self):
        password = self.validated_data('new_password')
        user = self.validated_data.get('user')
        user.set_password(password)
        user.save()