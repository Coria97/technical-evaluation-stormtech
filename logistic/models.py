from django.db import models

class Client(models.Model):
  name = models.CharField(max_length=30)
  email = models.EmailField()
  street = models.CharField(max_length=50)
  street_number = models.PositiveIntegerField()
  phone_number = models.CharField(max_length=30)
  
class Package(models.Model):
  PACKAGE_STATUS = [
    (0, 'Deposit'),
    (1, 'Distribution'),
  ]
  
  PACKAGE_TYPES = [
    ('P', 1000),
    ('M', 3000),
    ('G', 5000)
  ]

  tracking = models.PositiveIntegerField(unique=True)
  weight = models.FloatField()
  height = models.FloatField()
  status = models.IntegerField(choices=PACKAGE_STATUS, default=0)
  package_type = models.CharField(max_length=1, choices=PACKAGE_TYPES, default='P')
  client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
  
class Sheet(models.Model):
  sheet_number = models.PositiveIntegerField(unique=True)
  date = models.DateField()

class Report(models.Model):
  REPORT_STATUS = [
    ('B','Broken'),
    ('F','Factory Fault'),
    ('D','Delayed'),
  ]

  status = models.IntegerField(choices=REPORT_STATUS)
  title = models.CharField(max_length=30)
  description = models.CharField(max_length=255)

class ItemSheet(models.Model):
  position = models.CharField(max_length=50)
  sheet = models.ForeignKey(Sheet, on_delete=models.RESTRICT)
  package = models.ForeignKey(Package, on_delete=models.RESTRICT)
  failure_reasons = models.ForeignKey(Report, on_delete=models.RESTRICT)
