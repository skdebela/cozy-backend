from rest_framework import serializers

from destinations import models as basedata
from destinations.models import Destination


def create_basedata_serializer(basedata_model):
    class GenericSerializer(serializers.ModelSerializer):
        id = serializers.ReadOnlyField()

        class Meta:
            model = basedata_model
            fields = ["id", "name"]

    return GenericSerializer


StructureSerializer = create_basedata_serializer(basedata.Structure)
TypeSerializer = create_basedata_serializer(basedata.Type)
AmenitySerializer = create_basedata_serializer(basedata.Amenity)
StandoutAmenitySerializer = create_basedata_serializer(basedata.StandoutAmenity)
AccessibilityItemSerializer = create_basedata_serializer(basedata.AccessibilityItem)
SafetyConsiderationSerializer = create_basedata_serializer(basedata.SafetyConsideration)
SafetyDeviceSerializer = create_basedata_serializer(basedata.SafetyDevice)
PropertyInformationSerializer = create_basedata_serializer(basedata.PropertyInformation)
CheckoutInstructionSerializer = create_basedata_serializer(basedata.CheckoutInstruction)


class DestinationSerializer(serializers.ModelSerializer):
    # Serializers for related fields
    structure = serializers.PrimaryKeyRelatedField(queryset=basedata.Structure.objects.all())
    type = serializers.PrimaryKeyRelatedField(queryset=basedata.Type.objects.all())
    amenities = serializers.PrimaryKeyRelatedField(queryset=basedata.Amenity.objects.all())
    standout_amenities = serializers.PrimaryKeyRelatedField(queryset=basedata.StandoutAmenity.objects.all())
    accessibility_items = serializers.PrimaryKeyRelatedField(queryset=basedata.AccessibilityItem.objects.all())
    safety_considerations = serializers.PrimaryKeyRelatedField(queryset=basedata.SafetyConsideration.objects.all())
    safety_devices = serializers.PrimaryKeyRelatedField(queryset=basedata.SafetyDevice.objects.all())
    property_information = serializers.PrimaryKeyRelatedField(queryset=basedata.PropertyInformation.objects.all())
    checkout_instructions = serializers.PrimaryKeyRelatedField(queryset=basedata.CheckoutInstruction.objects.all())

    class Meta:
        model = Destination
        fields = [
            "id",
            "description",
            "host",
            "instant_book",
            "structure",
            "type",
            "amenities",
            "standout_amenities",
            "accessibility_items",
            "wifi_network_name",
            "wifi_password",
            "house_manual",
            "bedrooms",
            "beds",
            "bathrooms",
            "guests",
            "pets_allowed",
            "events_allowed",
            "smoking_allowed",
            "commercial_photography_allowed",
            "check_in_start_time",
            "check_in_end_time",
            "check_out_time",
            "additional_rules",
            "nightly_price",
            "new_listing_promotion",
            "weekly_discount_percentage",
            "monthly_discount_percentage",
            "cleaning_fee",
            "street_address",
            "apt_floor_bldg",
            "city",
            "province_state_territory",
            "postal_code",
            "google_calendar_locator",
            "directions",
            "safety_considerations",
            "safety_devices",
            "property_information",
            "check_in_method",
            "other_check_in_method",
            "checkout_instructions",
            "additional_checkout_instructions",
            "cancellation_policy",
        ]
        read_only_fields = ["host"]
