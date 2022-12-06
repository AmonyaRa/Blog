from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from applications.account.views import UserRegisterApiView

urlpatterns = [
    path('register/', UserRegisterApiView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view())
]
