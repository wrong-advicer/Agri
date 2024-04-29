from django.db import models
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as auth_login
# Create your models here.

class Add_profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True,blank=True)
    place=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    image=models.ImageField(upload_to='imagefile/',null=True,blank=True)

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url
    


class Product(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    priceD=models.IntegerField(null=True,blank=True)
    priceH=models.IntegerField(null=True,blank=True)
    spec=models.CharField(max_length=100,null=True,blank=True)
    desc=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to='imagefile/',null=True,blank=True)



    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url
    
    
class Rent(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    equipment=models.ForeignKey(Product, on_delete=models.CASCADE,null=True,blank=True)
    Status=models.BooleanField(default=False)
    Hour=models.IntegerField(null=True,blank=True)
    Day=models.IntegerField(null=True,blank=True)
    Date=models.DateField(null=True,blank=True)
    Proof=models.ImageField(upload_to='product_images/',null=True,blank=True)

    @property
    def imageURL(self):
        try:
            url=self.Proof.url
        except:
            url=''
        return url
    

class Testi(models.Model):
    user=models.ForeignKey(Add_profile, on_delete=models.CASCADE,null=True,blank=True)
    text=models.TextField(null=True,blank=True)  


    @property
    def imageURL(self):
        try:
            url=self.user.image.url
        except:
            url=''
        return url