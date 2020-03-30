from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
from .serializer import (SessionSerializer,
                         SessionCreateSerializer,
                         IncidentsSerializer,
                         TokenSerializer,
                         IncidentsAllSerializer)
from .models import ControlLogin, Incidents
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000


class SessionViewSet(ModelViewSet):
    serializer_class = SessionCreateSerializer
    queryset = ControlLogin.objects.all()

    def get_queryset(self):
        return self.filter_queryset(self.queryset)

    def __get_user_id(self, headers):
        token_queryset = Token.objects.filter(key=headers['Authorization'].split(' ')[-1])
        user = TokenSerializer(token_queryset, many=True)
        return user.data[0]['user']

    @action(methods=['get'], detail=False)
    def my_profile(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().filter(id_ong=self.__get_user_id(request.headers)))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        password = make_password(request.data['password'])
        request.data.update({'password': password})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            "username": serializer.data['username'],
            "email": serializer.data['email'],
            "phone_number": serializer.data['phone_number'],
            "city": serializer.data['city'],
            "uf": serializer.data['uf']
        }, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class IncidentViewSet(ModelViewSet):
    serializer_class = IncidentsSerializer
    queryset = Incidents.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def __get_user_id(self, headers):
        token_queryset = Token.objects.filter(key=headers['Authorization'].split(' ')[-1])
        user = TokenSerializer(token_queryset, many=True)
        return user.data[0]['user']

    def get_queryset(self):
        return self.filter_queryset(self.queryset)

    def create(self, request, *args, **kwargs):
        request.data['ong_id'] = self.__get_user_id(request.headers)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().filter(ong_id=self.__get_user_id(request.headers)))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        username = SessionSerializer(ControlLogin.objects.filter(id_ong=self.__get_user_id(request.headers)), many=True)
        if str(instance.ong_id) != username.data[0]['username']:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        print(instance.ong_id)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class IncidentsAllViewSet(ModelViewSet):
    queryset = Incidents.objects.all()
    serializer_class = IncidentsAllSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return self.filter_queryset(self.queryset)
