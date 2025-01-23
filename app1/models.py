from django.db import models

# Create your models here.z
class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    

class Estate(models.Model):
    name = models.CharField(max_length=100)
    capacity =models.IntegerField()
    free =models.IntegerField()
    rating =models.CharField(max_length=5)
    '''distance=models.FloatField()'''
    
    pic=models.ImageField(blank=False, null=True)
    

class Recentposts(models.Model):
    name=models.CharField( max_length=50)
    info=models.CharField( max_length=1000000) 
    author=models.CharField( max_length=50)
    data_aos= models.IntegerField() 






