from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import UserViewSet, VirtualMachineViewSet, ServerViewSet, DomainViewSet, HistoryViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'virtualmachines', VirtualMachineViewSet)
router.register(r'servers', ServerViewSet)
router.register(r'domains', DomainViewSet)
router.register(r'history', HistoryViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/', include(router.urls)),
]