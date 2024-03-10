import requests
import json

from django.template import loader
from django.shortcuts import render, HttpResponse, redirect

from .models import productname, user , adminaccount, adminaccounts

from .forms import UserForm, Usersignin
from django.templatetags.static import static

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import subprocess

from steam import Steam
from decouple import config


url = ("https://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=2071920&count=3&maxlength=300&format=json")



# Create your views here.

result = ['hey','hi','ho']
emailst = 'blank'
username = 'blank'
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
   
   print (username)
   
   requestpost = requests.get(url, params=req)
   response_data = requestpost.json()
   
  
   
   group = response_data["appnews"]
   group2 = group["newsitems"]
   
   addeddivst = {}
   addeddivss = {}
   
   for appnew in group2:
     addeddivss.update({(appnew["title"]) : (appnew["contents"])})

     # this is good for arrays for future refrence
     #addeddivst.append(appnew["title"])
     #addeddivss.append(appnew["contents"])
     
     
   
       # return redirect ('/signin')
       # print(authenticated)
     
    

   return render(request, "Homepage.html", {'addeddivss' : addeddivss})
    

def userfield(request):
    formal = UserForm()
    #if request.method == "GET" :
    
        
    
    
        #x = result[2]
        #upperword = [char for char in username if char.isupper()]
        #sandal = list(reversed(upperword))
        #socks = ''.join(sandal)
       # for char in username :
            #if char.isupper() :
       
        #print(list(reversed(result)))
        #for x in result :
        #    if x == 2 :
                #print(x)
        
     
    
    if request.method == "POST" : 
        formal = UserForm(request.POST or None)
       
        if formal.is_valid():       
            User.email = formal.cleaned_data['email']
            User.password = formal.cleaned_data['password']
            User.first_name = formal.cleaned_data['firstname']
            User.last_name = formal.cleaned_data['lastname']
            User.username = formal.cleaned_data['username']
                      
            print(User.password)
            
            user = User.objects.create_user(email=formal.cleaned_data['email'],username =formal.cleaned_data['username'],password=formal.cleaned_data['password'],
                                             first_name=formal.cleaned_data['firstname'], last_name=formal.cleaned_data['lastname']   )
            
            formal = UserForm()
            
    

        
        #word = request.POST.get('name')    
        #print(word)
    context = {'formal' : formal}
    return render(request, "signup.html",context)
    
    
def check(request) :

    formal = Usersignin()
    
    if request.method == "POST" : 
        formal = Usersignin(request.POST or None)
        
        if formal.is_valid():
            data = formal.cleaned_data
            username = data['username']
            password = data['password']
            #mydata = adminaccount.objects.filter(username = 'g').values()
            check_if_user_exists = User.objects.filter(username=username).exists()         
           
            if check_if_user_exists:      
                user = authenticate(request, username=username, password=password)
                        
                if user is not None:
                    print('success')
                    
                    request.session.set_expiry(500)
                    return redirect ('/')
            else:
                print('username')
    
   
    context = {'formal' : formal}

    return render(request, "signin.html",context)
    
    
def checkcredentials() :
    email
    mydata = adminaccount.objects.filter(email = emailst).values()
    