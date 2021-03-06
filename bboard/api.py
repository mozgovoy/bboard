from .models import Bb, CustomUser, Rubric
from rest_framework import viewsets, permissions
from .serializers import BbSerializer, RubricSerializer, BbListRetrieveSerializer, UsersSerializer
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS, IsAdminUser

class BbViewSet(viewsets.ModelViewSet):
    queryset = Bb.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=BbSerializer

    action_to_serializer = {
        "list":BbListRetrieveSerializer,
        "retrieve":BbListRetrieveSerializer
    }
    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action, self.serializer_class
        )

class RubricViewSet(viewsets.ModelViewSet):
    queryset = Rubric.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=RubricSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes=[IsAuthenticated ]
    serializer_class=UsersSerializer
