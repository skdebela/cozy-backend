from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('', include('djoser.urls.base')),
    path('users/token/create/', TokenObtainPairView.as_view(), name='jwt-token-create'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='jwt-token-refresh'),
    path('users/token/verify/', TokenVerifyView.as_view(), name='jwt-token-verify'),
]
