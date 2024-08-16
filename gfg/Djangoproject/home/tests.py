

from .models import Customer
from .models import Product
from .models import Cartitem
from .models import Cart




def getAllCustomers():
    customers = Customer.objects.all()

    list = []


    for cus_obj in customers:
        print(cus_obj.id)
     
        list.append(cus_obj.id)
    print(list)        
   

def getAllProducts():
    product = Product.objects.all()

    proli = []


    for pro_obj in product: 
        print(pro_obj.id)
     

        proli.append(pro_obj.id)
    print(proli)  


def getCartItems():
    cartitem = Cartitem.objects.all()  
    
    cartli = []
   

    for cart_obj in cartitem:
        print(cart_obj.id)

        cartli.append(cart_obj.id)
    print(cartli)  
        
        
def CreateCustomer():
    customer = Customer.objects.create()

    print(customer.id)    

def GetCartItems(cartid):
    cartitem = Cartitem.objects.filter(cart_id=cartid)

    carli = []

    for cartid in cartitem:
        print(cartid.id)   

        carli.append(cartid.id) 
    print(carli)

def GetCustomerItems2(customer_id):    
    # when you want to go any id in the models so we can use double underscore 


    #cartitem = Cartitem.objects.filter(cart__customer_id=customer_id) 
    customer = Customer.objects.get(id=customer_id)
    cart = Cart.objects.get(customer_id=customer.id)   
    cartitem = Cartitem.objects.filter(cart_id=cart.id)
    
    carli = []
    for x in cartitem:
        print(x.id)
        carli.append(x.id)
    print(carli)    

    print(cartitem)  

    return carli

def GetCartItems3(customer_id):  
    customer = Customer.objects.get(id=customer_id) 
    cart = Cart.objects.get(customer_id=customer.id)
    cartitem = Cartitem.objects.filter(cart_id=cart.id,product__is_active=True)
    
    carli = []
    for x in cartitem:
           carli.append(x.id)
    print(carli)    
    
def GetProductItems2(product_id):
    product = Product.objects.get(id=product_id)
    
        
    if  product.is_active == True:
        product.is_active = False
    else:  
        product.is_active = True
           
    return product.id

def GetProductUpdate3(product_id,desc,color,price):
    
    product = Product.objects.get(id=product_id)
    product.desc = desc
    product.color = color
    product.price = price
    product.save()
    
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 
       
       
        
    
    
    
    

             
          
          
        
    
    
    
            
        
        
              
        
       
          
        

           
        
          
        
          


     
     
    

    
    
        
           
        
        
        
        
        
     
        
       

    
    
    
                   
    
        

    

    




