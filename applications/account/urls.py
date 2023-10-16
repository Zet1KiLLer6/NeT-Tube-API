from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('activate/<uuid:code>/', ActivationAPIView.as_view()),

    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),

    path('forgot_password', ForgotPasswordAPIView.as_view()),
    path('reset_password', ForgotPasswordConfirmAPIView.as_view())
]