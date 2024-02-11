from django.db import models
from logistic.utils import PackageStatus, PackageType, ReportStatus

class Client(models.Model):
  name = models.CharField(max_length=30)
  email = models.EmailField()
  street = models.CharField(max_length=50)
  street_number = models.PositiveIntegerField()
  phone_number = models.CharField(max_length=30)
  
  def __str__(self):
    return self.name

class Package(models.Model):
  tracking = models.PositiveIntegerField(unique=True)
  weight = models.FloatField()
  height = models.FloatField()
  status = models.IntegerField(choices=PackageStatus.choices(), default=PackageStatus.DEPOSIT)
  package_type = models.CharField(max_length=10, choices=PackageType.choices(), default=PackageType.SMALL.label)
  client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
  
class Sheet(models.Model):
  sheet_number = models.PositiveIntegerField(unique=True)
  date = models.DateField()

class Report(models.Model):
  status = models.CharField(max_length=3, choices=ReportStatus.choices())
  title = models.CharField(max_length=30)
  description = models.CharField(max_length=255)

class ItemSheet(models.Model):
  position = models.CharField(max_length=50)
  sheet = models.ForeignKey(Sheet, on_delete=models.RESTRICT)
  package = models.ForeignKey(Package, on_delete=models.RESTRICT)
  failure_reasons = models.ForeignKey(Report, on_delete=models.SET_NULL, null=True, blank=True)
