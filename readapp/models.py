from email.policy import default
from statistics import mode
from django.db import models

# Create your models here.



class Country(models.Model):
    name	= models.CharField(max_length=20)

  

    # iso3	= models.CharField(max_length=20)
    # iso2	= models.CharField(max_length=20)
    # numeric_code	= models.IntegerField()
    # phone_code	= models.CharField(max_length=20)
    # capital=  models.CharField(max_length=20)
    # currency	= models.CharField(max_length=20)
    # currency_name	=  models.CharField(max_length=20)
    # currency_symbol	 =  models.CharField(max_length=20)
    # tld	 =  models.CharField(max_length=20)
    # native	  =  models.CharField(max_length=20)
    # region	 =  models.CharField(max_length=20)
    # subregion	=  models.CharField(max_length=20)
    # timezones	=  models.CharField(max_length=255)
    # latitude	= models.FloatField()
    # longitude	= models.FloatField()

    # def __str__(self):
    #     return self.name


   
    






#https://stackoverflow.com/questions/66128189/how-to-upload-a-csv-file-in-django-using-the-rest-api


#https://towardsdatascience.com/use-python-scripts-to-insert-csv-data-into-django-databases-72eee7c6a433