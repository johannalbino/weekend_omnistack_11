from rest_framework.serializers import ModelSerializer
from .models import ControlLogin, Incidents
from rest_framework.authtoken.models import Token


class SessionCreateSerializer(ModelSerializer):

    class Meta:
        model = ControlLogin
        fields = ['username', 'photo', 'email', 'password', 'phone_number', 'city', 'uf']


class SessionSerializer(ModelSerializer):

    class Meta:
        model = ControlLogin
        fields = ['username', 'email', 'phone_number', 'city', 'uf']


class IncidentsSerializer(ModelSerializer):

    class Meta:
        model = Incidents
        fields = ['id_incidents', 'title_incident', 'description_incident', 'value_incident', 'ong_id']


class IncidentsAllSerializer(ModelSerializer):
    ong_id = SessionSerializer(many=False)

    class Meta:
        model = Incidents
        fields = ['id_incidents', 'title_incident', 'description_incident', 'value_incident', 'ong_id']


class TokenSerializer(ModelSerializer):

    class Meta:
        model = Token
        fields = '__all__'
