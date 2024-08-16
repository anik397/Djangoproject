from django.shortcuts import render
#from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate,login,logout
#from rest_framework import viewsets
import json
from django.http import JsonResponse
from home.models import Report




def login_api(request):
    if request.method == 'POST':
        try:
            if not request.body:
                return JsonResponse({'error': 'No data provided'},status='failure')
            
            body = json.loads(request.body)
            
        except: 
            json.JSONDecodeError
            return JsonResponse({'message': 'Invalid JSON data', 'status': 'failure'}, status=400)
              
        username = body.get('username')
        password = body.get('password')
        
        user = authenticate(request,username=username,password=password)
            
    if user is not None:
        login(request,user)
        return JsonResponse({'messeage':'Login successfully'},status=200)
    
    else:
        return JsonResponse({'messeage':'Invalid credential'},status=401)
            
            
def logout_api(request):
    if request.method == 'POST':
        try:
            if not request.body:
               return JsonResponse({'messeage':'Logout successfully'},status=200)
            
            body = json.loads(request.body)
            
        except:
            json.JSONDecodeError
            return JsonResponse({'messeage':'Invalid Json data'},status=200)
        
        username = body.get('username')
        password = body.get('password')
        
        user = authenticate(username=username,password=password)
        
        if user is not None:
            logout(request)
            return JsonResponse({'messeage':'Logout successfully'},status=200)
            
        else:
            return JsonResponse({'messeage':'Invalid Credential'},status=200)
            

def createReport_api(request):
    if request.method == 'POST':
        body = json.loads(request.body) if any([isinstance(request.body,str),isinstance(request.body,bytes)]) else request.body      
        reportname = body.get('reportname')
        cc = body.get('cc')
        bcc = body.get('bcc')
        to = body.get('to')
        #return JsonResponse({'reportname':reportname,'cc':cc,'bcc':bcc,'to':to},status=200)
       
        report = Report.objects.create(reportname=reportname,cc=cc,bcc=bcc,to=to)
        
        if report is not None:
            return JsonResponse({'messeage':'Report created successfully'},status=200)
        
        else:
            return JsonResponse({'messeage':'Report creation failed'},status=400)
        
        
        
        
            
        
        
        


        
    
    
    
    
    
        
        
        
        
    
    
                    
            
           
                        
            
        
             
                           
              

                
            
            
            
            
            
            
            
            
            
    
    
    
       
    
                
      
        
        
    



        
        
        

# Create your views here.
