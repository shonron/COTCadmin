from django.db import models

# Create your models here.

class productname :
    price : float
    name : str
    img : str
    desr: str
    identify : int
    
class user :
    price : float
    name : str
    img : str
    desr: str
    identify : int
    
class adminaccount(models.Model) :
    firstname = models.CharField(max_length = 20, default="")   
    lastname = models.CharField(max_length = 20 , default="")
    username = models.CharField(max_length = 30, default="")
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length = 14)
    position = models.CharField(max_length=18)
    
class adminaccounts(models.Model) :
   
    username = models.CharField(max_length = 30, default="")
    password = models.CharField(max_length = 14)
       
    

    