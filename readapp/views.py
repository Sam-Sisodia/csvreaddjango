
from os import set_inheritable
import re
from django.shortcuts import render,HttpResponse

# Create your views here.
from rest_framework .views import  APIView
from rest_framework import generics
from rest_framework import status
from .  models import *
from .serializer import *
from rest_framework.response import Response
import pandas as pd 
import csv

class countrydetails(generics.CreateAPIView):
    serializer_class = fileuploadserilizer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for index ,row in reader.iterrows():
            _, created = Country.objects.get_or_create(
                name= row['name'])

        return Response({"status": "success"},
                        status.HTTP_201_CREATED)






# class countrydetails(ListCreateAPIView  ):
#     serializer_class = fileserilizer
#     queryset = ""

#     def post(self,request):
#         df=pd.read_csv('country.csv')
#         data = pd.DataFrame(df)
#         data.save()
#         return HttpResponse("Done")


    

  
    # if serilizer.is_valid():
    #     for index ,row in dataframe.iterrows():
    #         _, created = Country.objects.get_or_create(
    #             name= row['name'])


        

    #     serilizer.save()
    #     return HttpResponse("Done")
    # else:
     

        
        


        


# def import_data_csv(request,):
#     df=pd.read_csv('country.csv')
#     data = pd.DataFrame(df)




    














#     df=pd.read_csv('country1.csv',delimiter=";")
#    # print(df)
#     for index ,row in df.iterrows():
#         print(row)
#         # p
#         # ss =Country.objects.create(
#         #     name = row.name
            

#         # )

#         # print(ss)

    









    # for index ,row in dictionary.iterrows():
    #     print(row)
    

    
   
          
      

        
    



    # uu =Country.objects.bulk_create(model_instances)
    # uu.save()
   









'''
def import_data_csv(request,):
    with open("/home/visiontrek-pc/Sajal/ProjectCSV/country1.csv") as f:                         #https://stackoverflow.com/questions/2459979/how-to-import-csv-data-into-django-models
        reader = csv.reader(f)
        next(f)
        for row in reader:
            _, created = Country.objects.get_or_create(

                
                name=row[0],
                address=row[1],
            
                
            )
                 

'''

'''



def import_data_csv(request,):
    df=pd.read_csv('country.csv')
    data = pd.DataFrame(df)

    for index ,row in data.iterrows():
        _, created = Country.objects.get_or_create(
                        name = row['name'],
                        iso3  =  row['iso3'],
                        iso2 = row['iso2'],
                        numeric_code   = row['numeric_code'],
                        phone_code   = row['phone_code'],
                        capital   = row['capital'],
                        currency    = row['currency'],
                        currency_name    = row['currency_name'],
                        currency_symbol   = row['currency_symbol'],
                        tld   = row['tld'],
                        native   = row['native'],
                        region    = row['region'],
                        subregion   = row['subregion'],
                        timezones    = row['timezones'],
                        latitude   = row['latitude'],
                        longitude   = row['longitude'], )

                       

                       # for index, row in row_iter


    return HttpResponse("Done")
'''



#https://baronchibuike.medium.com/how-to-read-csv-file-and-save-the-content-to-the-database-in-django-rest-256c254ef722

