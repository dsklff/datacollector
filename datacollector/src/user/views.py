from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import action, permission_classes
from rest_framework.parsers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from requests import Request
from rest_framework.views import APIView

from .models import Teacher, Profile, Activation
from .serializers import TeacherSerializer, ProfileShortSerializer, ProfileFullSerializer,\
    TeacherRegisterSerializer, ChangePasswordSerializer
from rest_framework import viewsets, status


class TeacherViewSet(viewsets.GenericViewSet):
    queryset = Teacher.objects.all()
    http_method_names = ['get', 'post']
    serializer_class = TeacherRegisterSerializer

    @action(detail=False, methods=['post'])
    def register(self, request, pk=None):
        serializer = TeacherRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            activation = Activation.objects.create(user=user)
            params = {
                'id': user.activation.id,
            }
            r = Request('GET',
                        f'{request.build_absolute_uri("/")}user/activate/',
                        params=params) \
                .prepare()
            send_mail(
                subject='Account verification',
                message='To activate your account click link below\n' + r.url,
                from_email='doskuloff@gmail.com',
                recipient_list=[serializer.data.get('kbtu_mail'), ],
                fail_silently=False,
            )
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def activate(self, request, pk=None):
        id = request.GET.get('id')
        try:
            activation = Activation.objects.get(id=id)
        except Activation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if not activation.is_active:
            return Response({"Success": 'User is already activated'}, status.HTTP_200_OK)
        if activation.user:
            activation.is_active = False
            user = activation.user
            user.is_active = True
            activation.save()
            user.save()
            return Response({"Success": "Your account is now activated!"}, status=status.HTTP_200_OK)
        return Response({"Error": 'User not found'}, status.HTTP_404_NOT_FOUND)


class UpdatePassword(APIView):
    permission_classes = (IsAuthenticated, )

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer

        if serializer.is_valid():
            old_password = serializer.data['old_password']
            if not self.object.check_password(old_password):
                return Response({"old_password": ["Wrong password."]},
                                status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data['new_password'])
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updates successfully.',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileViewSet(viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    http_method_names = ['get', 'put', 'patch']
    parser_classes = (FormParser, MultiPartParser, JSONParser)
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=['get'])
    def get_profile(self, request):
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProfileFullSerializer(profile,
                                            context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['put', 'patch'])
    def edit_profile(self, request, pk=None):
        try:
            profile = Profile.objects.get(id=request.user.profile.id)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProfileFullSerializer(instance=profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
