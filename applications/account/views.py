from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.account.serializers import *

User = get_user_model()


class RegisterAPIView(APIView):
    def post(selfself, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('Регистрация прошла успешно! Ссылка для подтверждения была отправлен вам на почту.', status=201)
