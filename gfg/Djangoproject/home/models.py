from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
#from django.contrib.auth.models import AbstractUser
#from django.conf import settings
from django.contrib.auth import get_user_model

#from django.contrib import messages
from django.contrib.auth import authenticate



class CustomerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(age__gt=25)

class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50,blank=True,null=True)
    age = models.CharField(max_length=10,blank=True,null=True )
     
    objects = CustomerManager()
    
    def __str__(self):
        return self.name
    
    


class Product(models.Model):
    name = models.CharField(max_length=50) 
    desc = models.CharField(max_length=50,blank=True,null=True) 
    color = models.CharField(max_length=50 ,blank=True,null=True) 
    price = models.CharField(max_length=50,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    


def __str__(self):
            return f'{str(self.name)}- {str(self.id)}-'   

    
    



class Cart(models.Model):
    
    total_price= models.CharField(max_length=50,blank=True,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True,null=True)

    
    def __str__(self):
         return f'{str(self.customer)}- {str(self.customer.id)}-'   


    
class Cartitem(models.Model):
    total_quantity= models.CharField(max_length=50,blank=True,null=True) 
    category = models.CharField(max_length=50,blank=True,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,blank=True,null=True)

    
    def __str__(self):

        return str(self.id)
class Order(models.Model):
    pricing= models.CharField(max_length=50,blank=True,null=True) 
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True,null=True)


    def __str__(self):

        return str(self.customer)

class OrderItem(models.Model):
    deleivery = models.CharField(max_length= 10,blank = True,null=True)
    order = models.ForeignKey(Order,max_length=20,on_delete=models.CASCADE,blank=True,null=True)
    product =models.ForeignKey(Product,max_length=50,on_delete=models.CASCADE,blank=True,null=True)
    category = models.CharField(max_length=30,blank= True,null=True)  
    
    def __str_(self):
        return str(self.name)  
    

class Post(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    author = models.CharField(max_length=100,blank=True,null=True)
    slug = models.CharField(max_length=20,blank=True,null=True)
    
#class User(AbstractUser):
    #nickname = models.CharField(max_length=255,blank=True,null=True)
    #wallet = models.FloatField(blank=True,null=True)
   
    
    #def _str_(self):
        #return self.username
        

            
        
         
    
    
#class CustomMixins(models.Model):    
    #status = models.BooleanField(default=True)
    #created_at = models.DateTimeField(auto_now_add=True) 
     #updated_at = models.DateTimeField(default = datetime.now)
     #created_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name = 'reports_created')   
     #updated_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='reports_updated')
     #is_deleted = models.BooleanField(default=False)
        
     #class Meta:
         #abstract = True
        
        
class Report(models.Model):
        
    
     reportname = models.CharField(max_length=20,blank=True,null=True)
     to = models.CharField(max_length=355,blank=True,null=True)
     cc = models.CharField(max_length=355,blank=True,null=True)
     bcc = models.CharField(max_length=355,blank=True,null=True)
     
     
    
    

    
    
     
     
     
    

    

def userlist(username,password):
    #User = get_user_model
    #querysetusers = User.objects.filter(username=username,password=password)
    #print(querysetusers)
    
    user = authenticate(username = username, password = password)
    
    print(user)
    
    if user is not None and user.is_authenticated:
    
        print(f'{user.first_name} You are logged successfully')
           
    else:
        print('Invalid credential') 
        
        
def registeruser(first_name,last_name,username,password):
    user = User.objects.create(first_name=first_name,last_name=last_name,username=username,password=password)

    user = authenticate(username=username,password=password)
    print(user)
    
    if user is not None and user.is_authenticated:
        print('Username is successfully created')
        
        
    else:
        print('Something went wrong') 
        
def updateuser(user_id,first_name,last_name):
   # user = User.objects.create(first_name=first_name,last_name=last_name,username=username,password=password)
   # user = User.objects.filter(id=user_id).update(first_name=first_name,last_name=last_name)
    
    user = User.objects.get(id=user_id)
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    
   #print(user)
    
    
    
    #if user is not None :
        #print('Username is successfully updated')
    #else:    
       # print('Something went wrong') 
       
def getuser(user_id):
    user = User.objects.filter(id=user_id).values('username','first_name','last_name') 
    print(user)
    
    
def getli():
    users = User.objects.all()
    
    my_li=[]
    
        
    my_dict = {}
    for user in users:
        my_dict[user.username,user.first_name,user.last_name] = {   
        'username':user.username,
        'first_name':user.first_name,
        'last_name':user.last_name,
        
        
    }
       
    my_li.append(my_dict)  
    return my_li 

def mylogin(username,password):
    
    user = authenticate(username=username,password=password)
    print(user)

    if user is not None:
        #login(user)
        print('User is successfully login')
        
    else:
        print('Invalid user')     
    
    
def mylogout(username,password):
    
    user = authenticate(username=username,password=password)
    print(user)

    if user is not None:
        #login(user)
        print('User is successfully logout')
        
    else:
        print('Invalid user')  
        
          
          
          
        
         
        

     
     
            
            
        

    
            
        
 
    
    
    
    
    
    
    
     
    
    
    
    
    
          
          
                
        
        
        
        
        
        
        
        
        
        
        
        
           
    
    
    
    
            
        
                 
           

    
    
    
    
 
    
    
    
    
    
    

    
    
    
    
    
    

        


    

    
    
    
    
    
        
        
    
    
    
    

    
    
    
    
    
        
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
        
    
          
     
         
         
        


 
