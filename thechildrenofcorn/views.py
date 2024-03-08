import requests
import json


from django.shortcuts import render, HttpResponse

from .models import productname, user 

from .forms import UserForm
from django.templatetags.static import static

import subprocess

from steam import Steam
from decouple import config


url = ("https://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=2071920&count=3&maxlength=300&format=json")



# Create your views here.

result = ['hey','hi','ho']
username = 'BlAnk'
#checkresult = result.split()
password = "studytonight"
word = 'nothing'
passwordar = [char for char in password]
file = static("code.txt")


req = {
    "Key": "68F1DF313D6C8D7CAF07D4F6717A20A3",
    "appid": "2071920",
    "listingid": "5430731906064702783"
    }



def start(request) :
   
   ##r = requests.get(url, params=req)
   
   ##print(r.text)
   
   requestpost = requests.get(url, params=req)
   response_data = requestpost.json()
   
   print(type(response_data))
   
   group = response_data["appnews"]
   group2 = group["newsitems"]
   
   addeddivst = {}
   addeddivss = {}
   
   for appnew in group2:  

     # this is good for arrays for future refrence
     #addeddivst.append(appnew["title"])
     #addeddivss.append(appnew["contents"])
     
     addeddivss.update({(appnew["title"]) : (appnew["contents"])})
     
     
   print (addeddivss)

   return render(request, "Homepage.html", {'addeddivss' : addeddivss})
    

def userfield(request):
    formal = UserForm()
    if request.method == "GET" :
    
        
    
    
        #x = result[2]
        #upperword = [char for char in username if char.isupper()]
        #sandal = list(reversed(upperword))
        #socks = ''.join(sandal)
       # for char in username :
            #if char.isupper() :
        print(socks)
        #print(list(reversed(result)))
        #for x in result :
        #    if x == 2 :
                #print(x)
        
    
    
    if request.method == "POST" : 
        formal = UserForm(request.POST or None)
        if formal.is_valid():
            formal.save()
            formal = UserForm()
    

        
        #word = request.POST.get('name')    
        #print(word)
    context = {'formal' : formal}
    return render(request, "signin.html",context)
    
    
def check() :
    print()

    