from rest_framework import viewsets
from .models import Studentprofile
from .serializers import StudentProfilSerializer
from .serializers import ResetPasswordDemandeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework.generics import GenericAPIView
from django.contrib.auth import get_user_model
from core.lib.encode import encode_uid
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import get_template
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives


class StudentProfilViewSet(viewsets.ModelViewSet):
    queryset = Studentprofile.objects.all()
    serializer_class = StudentProfilSerializer


class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        if not email or not password:
            return Response({'isAuthenticated': False})
        user = authenticate(username=email, password=password)
        if user is None:
            return Response({'isAuthenticated': False})
        login(request=request, user=user)
        return Response({'isAuthenticated': True})


class LogoutView(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return
        logout(request=request)
        return Response({'isAuthenticated': False})


class CheckAuthView(APIView):
    permission_classes = []

    def get(self, request):
        if request.user.is_authenticated:
            return Response({'isAuthenticated': True})
        return Response({'isAuthenticated': False})


class ResetPasswordDemandeView(GenericAPIView):
    serializer_class = ResetPasswordDemandeSerializer
    permission_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            user = get_user_model().objects.get(email=email)
        context = {
            'uid': encode_uid(user.id),
            'token': default_token_generator.make_token(user)
        }

        html = get_template('accounts/reset_password.html')
        email_body = html.render(context)
        subject, from_email, to = "hello", "from@example.com", "to@example.com"
        msg = EmailMultiAlternatives(subject, email_body, from_email, [to])
        msg.content_subtype = "html"
        msg.send()
        return Response()
