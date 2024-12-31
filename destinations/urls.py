from django.urls import include, path
from rest_framework.routers import DefaultRouter

from destinations import views as destinations_views

router = DefaultRouter()
router.register(r"destinations", destinations_views.DestinationViewSet, basename="destination")

# basedata
basedata_router = DefaultRouter()
basedata_router.register(r"structures", destinations_views.StructureViewSet, basename="structure")
basedata_router.register(r"types", destinations_views.TypeViewSet, basename="type")
basedata_router.register(r"amenities", destinations_views.AmenityViewSet, basename="amenity")
basedata_router.register(r"standout-amenities", destinations_views.StandoutAmenityViewSet, basename="standout-amenity")
basedata_router.register(
    r"accessibility-items", destinations_views.AccessibilityItemViewSet, basename="accessibility-item"
)
basedata_router.register(
    r"safety-considerations", destinations_views.SafetyConsiderationViewSet, basename="safety-consideration"
)
basedata_router.register(r"safety-devices", destinations_views.SafetyDeviceViewSet, basename="safety-device")
basedata_router.register(
    r"property-information", destinations_views.PropertyInformationViewSet, basename="property-information"
)
basedata_router.register(
    r"checkout-instruction", destinations_views.CheckoutInstructionViewSet, basename="checkout-instruction"
)

urlpatterns = [
    path("", include(router.urls)),
    path("/basedata/", include(basedata_router.urls)),
]
