from django.shortcuts import render
from logistic.models import Package, ItemSheet
from logistic.serializers import PackageSheetSerializer, PackageSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class TrackingDetailsView(APIView):
  def get(self, request, tracking_number):
    try:
        package = get_object_or_404(Package, tracking=tracking_number)
        item_sheet = ItemSheet.objects.filter(package=package).first()
        serializer = PackageSheetSerializer(instance=item_sheet)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=400)
