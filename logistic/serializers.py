from rest_framework import serializers
from logistic.models import Package, Sheet, Client

class SheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sheet
        fields = ['sheet_number', 'date']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['name', 'email', 'street', 'street_number', 'phone_number']

class PackageSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Package
        fields = ['tracking', 'weight', 'height', 'status', 'package_type', 'client']

class PackageSheetSerializer(serializers.Serializer):
    package = PackageSerializer()
    sheet_number = serializers.IntegerField()

    def to_representation(self, instance):
        package_representation = PackageSerializer(instance.package).data
        sheet_number = instance.sheet.sheet_number if instance.sheet else None
        package_representation['sheet_number'] = sheet_number
        return package_representation
