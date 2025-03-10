from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User, VirtualMachine, Server, Domain, History
from core.serializers import UserSerializer, VirtualMachineSerializer, ServerSerializer, DomainSerializer, HistorySerializer

# API برای کاربر (User )
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # فقط کاربران احراز هویت شده می‌توانند به این API دسترسی داشته باشند


# API برای ماشین مجازی (VirtualMachine)
class VirtualMachineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows virtual machines to be viewed or edited.
    """
    queryset = VirtualMachine.objects.all()
    serializer_class = VirtualMachineSerializer
    permission_classes = [IsAuthenticated]


# API برای سرور (Server)
class ServerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows servers to be viewed or edited.
    """
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    permission_classes = [IsAuthenticated]


# API برای دامنه (Domain)
class DomainViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows domains to be viewed or edited.
    """
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    permission_classes = [IsAuthenticated]


# API برای تاریخچه (History)
class HistoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows history records to be viewed or edited.
    """
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = [IsAuthenticated]