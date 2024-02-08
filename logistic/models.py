from django.db import models

class Client(models.Model):
  name = models.CharField(max_length=30)
  email = models.EmailField()
  direction = models.CharField(max_length=50)
  phone_number = models.CharField(max_length=30)
  
class Package(models.Model):
  PACKAGE_STATUS = [
    (0, 'Deposit'),
    (1, 'Distribution'),
  ]
  
  PACKAGE_TYPES = [
    ('P', 'Small', 1000),
    ('M', 'Medium', 3000),
    ('G', 'Big', 5000)
  ]

  tracking = models.PositiveIntegerField(unique=True)
  weight = models.FloatField()
  height = models.FloatField()
  status = models.IntegerField(choices=PACKAGE_STATUS, default=PACKAGE_STATUS.first)
  package_type = models.CharField(max_length=1, choices=PACKAGE_TYPES, default=PACKAGE_TYPES.first)
  # relacion cliente
  
class Sheet(models.Model):
  sheet_number = models.PositiveIntegerField(unique=True)
  date = models.DateField()
  
class ItemSheet(models.Model):
  position = models.CharField(max_length=50)
  #relacion sheet package report


class Report(models.Model):
  REPORT_STATUS = [
    ('B','Broken'),
    ('F','Factory Fault'),
    ('D','Delayed'),
  ]

  status = models.IntegerField(choices=REPORT_STATUS)
  title = models.CharField(max_length=30)
  description = models.CharField()

