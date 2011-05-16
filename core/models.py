from django.db import models
from django.contrib.auth.models import User

class ActiveUsers(models.Model):
    ds = models.DateTimeField('partition date')
    userid = models.IntegerField()
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    regdate = models.DateTimeField('date registered')
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    city = models.CharField(max_length=100) 
    state = models.CharField(max_length=100) 
    country = models.CharField(max_length=100) 
    visited = models.DateTimeField('date registered') 
    seen = models.DateTimeField('date registered') 
    
class Quotes(models.Model):
    ds = models.DateTimeField('partition date')
    userid = models.IntegerField()
    quoteid = models.IntegerField()
    datestated = models.DateTimeField('date quoted')
    
class QuoteInfo(models.Model):
    ds = models.DateTimeField('partition date') 
    quoteid = models.IntegerField()
    quote_string = models.CharField(max_length=2000)
    
class QuoteLocation(models.Model):
    ds = models.DateTimeField('partition date')
    quoteid = models.IntegerField()
    lat = models.IntegerField()
    long = models.IntegerField()

class FollowerList(models.Model):
    ds = models.DateTimeField('partition date')
    userid = models.IntegerField()
    followerid = models.IntegerField()
    
class QuoteTag(models.Model): 
    ds = models.DateTimeField('partition date')
    quoteid = models.IntegerField()
    taggerid = models.IntegerField()
    tageeid = models.IntegerField()

# Create your models here.
