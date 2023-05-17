import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.

class Station(models.Model):
  id = models.CharField(max_length=40, primary_key=True)
  uid = models.CharField(max_length=4)
  name = models.CharField(max_length=150)
  slots = models.IntegerField()
  payment_terminal = models.BooleanField()
  has_ebike = models.BooleanField()
  
  @admin.display(
    description='Has e-bike?',
    boolean=True,
  )
  def has_ebike_bool(self):
    return self.has_ebike
  
  def __str__(self) -> str:
    return self.name
  
class Location(models.Model):
  id_station = models.ForeignKey(Station, on_delete=models.CASCADE)
  latitude = models.FloatField()
  longitude = models.FloatField()
  altitude = models.FloatField()
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=50)
  country = models.CharField(max_length=50)
  
  def __str__(self) -> str:
    return self.address
  
class PaymentType(models.Model):
  id = models.CharField(max_length=40, primary_key=True)
  name = models.CharField(max_length=100)
  
  def __str__(self) -> str:
    return self.name
  
class PaymentStation(models.Model):
  id_station = models.ForeignKey(Station, on_delete=models.CASCADE)
  id_payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
  
class StationState(models.Model):
  id_station = models.ForeignKey(Station, on_delete=models.CASCADE)
  empty_slots = models.IntegerField()
  normal_bikes = models.IntegerField()
  electric_bikes = models.IntegerField()
  renting = models.BooleanField()
  returning = models.BooleanField()
  last_update = models.DateTimeField()
  
  def was_recentrly_updated(self):
    now = timezone.now()
    return self.last_update >= now - datetime.timedelta(minutes=1)
  
  def has_disabled_bikes(self):
    return self.id_station.slots - self.empty_slots - self.normal_bikes - self.electric_bikes 
  
  def __str__(self) -> str:
    return self.id_station.name
  