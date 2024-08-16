from typing import Any
from django.contrib import admin
from django.apps import apps
from django.db.models.query import QuerySet
from django.http import HttpRequest
# from .models import *
from .models import Customer
from .models import Cartitem
#from django.contrib.auth.admin import UserAdmin
#from .models import User








TEXT = 'Some text that we can include'


models = apps.get_models('home')

#@admin.register(Customer)
class Customeradmin(admin.ModelAdmin):
       list_display = ('age','name','email')
       customer = Customer.objects.filter(age__lt=22)
       
class MyModelAdmin(admin.ModelAdmin):

     def queryset(self, request):
        qs = super(MyModelAdmin, self).queryset(request)
        return qs.filter(age__in=[18])
admin.site.register(Customer, MyModelAdmin)       
 


@admin.register(Cartitem)
class Cartadmin(admin.ModelAdmin):
        list_display = ('product','cart')
        list_select_related = ('cart',)
    

        def get_queryset(self, request):
              qs = super().get_queryset(request)
              return qs.select_related('cart', 'product')

#@admin.register(Customer)
class Customeradmin(admin.ModelAdmin):
        readonly_fields = ('name','phone','age')
        writeable_fields = ('email')

def has_delete_permission(self, request, obj=None):
             return False
           
class CustomerAdmin(admin.ModelAdmin):
    def has_delete_permission(self , request , obj=None):
         if request.user.is_superuser:
             return True
         return False



class CustomerInline(admin.StackedInline):
    model = Customer

class CartAdmin(admin.ModelAdmin):
    inlines = [CustomerInline]
    

#@admin.register(User)

#class UserAdminsite(UserAdmin):
   # model = User
    #fieldsets = UserAdmin.fieldsets + (
        #('None',{'fields':('nickname',)}),
        

    #fieldsets = UserAdmin.fieldsets + (
        #('None',{'fields':('wallet',)}),
        
 
    
#admin.site.register(UserAdmin)    
    
#for model in models:
       # try:
              # @admin.register(model)
              
               #class customization_model(admin.ModelAdmin):
                     # list_display= [field.name  for field in model._meta.fields ]
                      #search_fields = [field.name for field in model._meta.fields]
                      #list_filter = [field.name for field in model._meta.fields]
                     
                     
        #except admin.sites.AlreadyRegistered:
              # print('Already Registered')
               #pass



