from django.db import models

# Create your models here.


#items db
class Items(models.Model):
    
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    amount = models.IntegerField(max_length=4)
    