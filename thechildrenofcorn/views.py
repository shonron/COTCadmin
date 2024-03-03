

from django.shortcuts import render, HttpResponse

from .models import productname, user 

from .forms import UserForm
from django.templatetags.static import static

import subprocess



# Create your views here.

result = ['hey','hi','ho']
username = 'BlAnk'
#checkresult = result.split()
password = "studytonight"
word = 'nothing'
passwordar = [char for char in password]
file = static("code.txt")






def start(request) :
   
    
   

    return render(request, "Homepage.html")
    

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

    