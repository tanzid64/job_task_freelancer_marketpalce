from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.serializers import UserLoginSerializer, UserTokenRefreshSerializer

# Create your views here.
class UserLoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer
    
class UserTokenRefreshView(TokenRefreshView):
    serializer_class = UserTokenRefreshSerializer
