from rest_framework.response import Response
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from .serializers import CustomRegistrationSerializer, CustomLoginSerializer, CustomUserSerializer


class CustomLoginView(LoginView):
    serializer_class = CustomLoginSerializer

    def get_response(self):
        login_data = super(CustomLoginView, self).get_response()
        login_data.data['user'] = CustomUserSerializer(self.user).data
        return Response(login_data.data)


class SignupAPIView(RegisterView):
    serializer_class = CustomRegistrationSerializer

    def get_response_data(self, user):
        signup_data = super(SignupAPIView, self).get_response_data(user)
        signup_data['user'] = CustomUserSerializer(user).data
        return signup_data
