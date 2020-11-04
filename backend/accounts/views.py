from rest_framework import permissions, generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from knox.models import AuthToken
from django.contrib.auth.hashers import check_password
from django.http import QueryDict
from .serializers import CreateUserSerializer, UserSerializer, LoginUserSerializer, ProfileSerializer, UserPasswordSerializer
from .models import Profile, User


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)[1]
        return Response (
            {
                'user' : UserSerializer(
                    user, context = self.get_serializer_context()
                ).data,
                'token': token,
            }
        )

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                'user': UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                'token': AuthToken.objects.create(user)[1],
            }
        )


class UserAPI(generics.RetrieveAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class ProfileAPI(generics.GenericAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get(self, request, nickname):
        user = User.objects.get(nickname=nickname)
        profile = get_object_or_404(Profile, pk=user.id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    
    def put(self, request, nickname):
        user = User.objects.get(nickname=nickname)
        profile = get_object_or_404(Profile, pk=user.id)
        if type(request.data) == dict:
            ordinary_dict = request.data
            query_dict = QueryDict('', mutable=True)
            query_dict.update(ordinary_dict)
        else:
            query_dict = request.data
        serializer = ProfileSerializer(profile, data=query_dict)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        

        return Response(serializer.errors, status=400)
    
    def delete(self, request, nickname):
        user = User.objects.get(nickname=nickname)
        user.delete()
        return Response(True)


class RegistrationCheckAPI(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def get(self, request, checking):
        if User.objects.filter(nickname=checking).exists() or User.objects.filter(email=checking).exists():
            return Response(False)
        else:
            return Response(True)


class PasswordCheckAPI(generics.GenericAPIView):
    serializer_class = UserPasswordSerializer
    queryset = User.objects.all()

    def post(self, request, nickname):
        password = request.data['password']
        user = User.objects.get(nickname=nickname)
        if check_password(password, user.password):
            return Response(True)
        else:
            return Response(False)