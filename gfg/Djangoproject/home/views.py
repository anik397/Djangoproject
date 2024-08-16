from django.shortcuts import render
#from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate,login
#from rest_framework import viewsets
import json
from django.http import JsonResponse
#from .models import Report



def myview_set(request):
    if request.method == 'POST':
            body = json.loads(request.body)
            username = body.get('username')
            password = body.get('password')
        
            user = authenticate(request,username=username,password=password)
            
            
            if user is not None:
                login(request,user)
                return JsonResponse({'messeage':'Login successfully'},status=200)
    
            else:
                return JsonResponse({'messeage':'Invalid credential'},status=200)
            
            
            
            
            
            
            
            
            
            
    
    
    
       
    
                
      
        
        
    



        
        
        

# Create your views here.
