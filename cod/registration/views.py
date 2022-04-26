from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.decorators import api_view




class RegisterView(GenericAPIView):
   serializer_class = RegisterSerializer
   def post(self, request):
       data = request.data
       serializer = RegisterSerializer(data=data, context={'request': request})
       if serializer.is_valid(raise_exception=True):
           user = serializer.save()
           return Response('Регистрация пользователя прошла успешно!', status=status.HTTP_201_CREATED)



class LoginView(GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
        if not user:
            raise exceptions.AuthenticationFailed('Username or password are incorrect')

        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
        })


# class RegisterView(GenericAPIView):

#     serializer_class = RegisterSerializer

#     def post(self, request):
#         data = request.data
#         serializer = RegisterSerializer(data=data, context={'request': request})
#         if serializer.is_valid(raise_exception=True):
#             user = serializer.save()
#             # MyUser.objects.create(user=user)
#             return Response('Регистрация пользователя прошла успешно!', status=status.HTTP_201_CREATED)


# class LoginView(GenericAPIView):

#     serializer_class = LoginSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         print(serializer.validated_data)
#         # print(serializer.valid_data())
#         # user = serializer.validated_data
#         user = authenticate(username=serializer.validated_data['email'], password=serializer.validated_data['password'])
#         # user = authenticate(user)
#         print(user)
#         if not user:
#             raise exceptions.AuthenticationFailed('Username or password are incorrect')

#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email,
#         })



from rest_framework.views import APIView











# @api_view(["POST"])
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response({'error': 'Пожалуйста, укажите имя пользователя и пароль'},
#                         status=HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response({'error': 'Неверные учетные данные'},
#                         status=HTTP_404_NOT_FOUND)
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key},
#                     status=HTTP_200_OK)