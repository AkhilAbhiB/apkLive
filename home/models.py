from django.db import models

# Create your models here.

class re(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    msg = models.TextField()
    
    
class allapp(models.Model):
    appname = models.CharField(max_length=250)
    appurl = models.CharField(max_length=50000)
    appdow = models.CharField(max_length=50000)
    
    appsize = models.CharField(max_length=250)

class ss(models.Model):
    appname = models.CharField(max_length=250)
    appurl = models.CharField(max_length=50000)
    appdow = models.CharField(max_length=50000)
    
    appsize = models.CharField(max_length=250)
    
    
    
class edit(models.Model):
    appname = models.CharField(max_length=250)
    appurl = models.CharField(max_length=50000)
    appdow = models.CharField(max_length=50000)
    
    appsize = models.CharField(max_length=250)
    
    
class game(models.Model):
    appname = models.CharField(max_length=250)
    appurl = models.CharField(max_length=50000)
    appdow = models.CharField(max_length=50000)
    
    appsize = models.CharField(max_length=250)
    
    
    
class aa(models.Model):
    appname = models.CharField(max_length=250)
    appurl = models.CharField(max_length=50000)
    appdow = models.CharField(max_length=50000)
    
    appsize = models.CharField(max_length=250)
    appc = models.CharField(max_length=250)
    
    