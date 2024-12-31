from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, get_object_or_404

from core.permissions import IsAdminUserOrReadOnly
from destinations import models as basedata_models
from destinations import serializers as basedata_serializers
from destinations.models import Destination
from destinations.permissions import IsOwnerOrReadOnly
from destinations.serializers import DestinationSerializer

User = get_user_model()


def create_basedata_viewset(basedata_model, basedata_serializer_class):
    class GenericViewSet(viewsets.ModelViewSet):
        queryset = basedata_model.objects.all()
        serializer_class = basedata_serializer_class
        permission_classes = [IsAdminUserOrReadOnly]

    return GenericViewSet


StructureViewSet = create_basedata_viewset(basedata_models.Structure, basedata_serializers.StructureSerializer)
TypeViewSet = create_basedata_viewset(basedata_models.Type, basedata_serializers.TypeSerializer)
AmenityViewSet = create_basedata_viewset(basedata_models.Amenity, basedata_serializers.AmenitySerializer)
StandoutAmenityViewSet = create_basedata_viewset(
    basedata_models.StandoutAmenity, basedata_serializers.StandoutAmenitySerializer
)
AccessibilityItemViewSet = create_basedata_viewset(
    basedata_models.AccessibilityItem, basedata_serializers.AccessibilityItemSerializer
)
SafetyConsiderationViewSet = create_basedata_viewset(
    basedata_models.SafetyConsideration, basedata_serializers.SafetyConsiderationSerializer
)
SafetyDeviceViewSet = create_basedata_viewset(basedata_models.SafetyDevice, basedata_serializers.SafetyDeviceSerializer)
PropertyInformationViewSet = create_basedata_viewset(
    basedata_models.PropertyInformation, basedata_serializers.PropertyInformationSerializer
)
CheckoutInstructionViewSet = create_basedata_viewset(
    basedata_models.CheckoutInstruction, basedata_serializers.CheckoutInstructionSerializer
)


class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)


class UserDestination(ListAPIView):
    serializer_class = DestinationSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        user = get_object_or_404(User, pk=pk)

        return Destination.objects.filter(host=user)
