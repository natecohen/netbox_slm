from rest_framework.serializers import SerializerMethodField, HyperlinkedIdentityField

from netbox.api.serializers import NetBoxModelSerializer
from netbox_slm.models import SoftwareProduct, SoftwareProductVersion, SoftwareProductInstallation, SoftwareLicense


class SoftwareLicenseSerializer(NetBoxModelSerializer):
    display = SerializerMethodField()
    url = HyperlinkedIdentityField(view_name="plugins-api:netbox_slm-api:softwarelicense-detail")

    class Meta:
        model = SoftwareLicense
        fields = (
            "id",
            "display",
            "url",
            "name",
            "description",
            "type",
            "spdx_expression",
            "stored_location",
            "stored_location_url",
            "start_date",
            "expiration_date",
            "support",
            "license_amount",
            "software_product",
            "version",
            "installation",
            "tags",
            "comments",
            "custom_field_data",
            "created",
            "last_updated",
        )
        brief_fields = ("id", "display", "url", "name", "description")

    def get_display(self, obj):
        return f"{obj}"


class SoftwareProductSerializer(NetBoxModelSerializer):
    display = SerializerMethodField()
    url = HyperlinkedIdentityField(view_name="plugins-api:netbox_slm-api:softwareproduct-detail")

    class Meta:
        model = SoftwareProduct
        fields = (
            "id",
            "display",
            "url",
            "name",
            "description",
            "manufacturer",
            "description",
            "tags",
            "comments",
            "custom_field_data",
            "created",
            "last_updated",
        )
        brief_fields = ("id", "display", "url", "name", "description")

    def get_display(self, obj):
        return f"{obj}"


class SoftwareProductInstallationSerializer(NetBoxModelSerializer):
    display = SerializerMethodField()
    url = HyperlinkedIdentityField(view_name="plugins-api:netbox_slm-api:softwareproductinstallation-detail")

    class Meta:
        model = SoftwareProductInstallation
        fields = (
            "id",
            "display",
            "url",
            "device",
            "virtualmachine",
            "cluster",
            "software_product",
            "version",
            "tags",
            "comments",
            "custom_field_data",
            "created",
            "last_updated",
        )
        brief_fields = ("id", "display", "url")

    def get_display(self, obj):
        return f"{obj}"


class SoftwareProductVersionSerializer(NetBoxModelSerializer):
    display = SerializerMethodField()
    url = HyperlinkedIdentityField(view_name="plugins-api:netbox_slm-api:softwareproductversion-detail")

    class Meta:
        model = SoftwareProductVersion
        fields = (
            "id",
            "display",
            "url",
            "name",
            "description",
            "release_date",
            "documentation_url",
            "end_of_support",
            "filename",
            "file_checksum",
            "file_link",
            "release_type",
            "software_product",
            "tags",
            "comments",
            "custom_field_data",
            "created",
            "last_updated",
        )
        brief_fields = ("id", "display", "url", "name", "description")

    def get_display(self, obj):
        return f"{obj}"
