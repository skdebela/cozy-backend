from django.contrib import admin

from destinations.models import (
    AccessibilityItem,
    Amenity,
    CheckoutInstruction,
    Destination,
    PropertyInformation,
    SafetyConsideration,
    SafetyDevice,
    StandoutAmenity,
    Structure,
    Type,
)

models_to_register = [
    Structure,
    Type,
    Amenity,
    StandoutAmenity,
    AccessibilityItem,
    SafetyConsideration,
    SafetyDevice,
    PropertyInformation,
    CheckoutInstruction,
    Destination,
]

for model in models_to_register:
    admin.site.register(model)
