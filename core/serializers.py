from rest_framework import serializers
from core.models import User, VirtualMachine, Server, Domain, History

# Serializer برای مدل User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_admin', 'phone_number', 'created_at', 'updated_at']


# Serializer برای مدل VirtualMachine
class VirtualMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualMachine
        fields = ['id', 'name', 'technical_responsible', 'legal_responsible', 'created_at', 'updated_at']


# Serializer برای مدل Server
class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ['id', 'name', 'internal_ip', 'public_ip', 'virtual_machine', 'owner', 'open_ports', 'access_status', 'created_at', 'updated_at']


# Serializer برای مدل Domain
class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ['id', 'name', 'ssl_expiration_date', 'server', 'owner', 'created_at', 'updated_at']


# Serializer برای مدل History
class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['id', 'server', 'status', 'timestamp', 'notes']