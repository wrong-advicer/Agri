from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import os
from django.contrib.auth import authenticate,logout,login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# # Create your views here.



############################################# USER FUNCTION ##############################################


def index(request):
    cart=Product.objects.all()
    testimonials = Testi.objects.all()
    context={
        'var1':cart,
        'testimonials':testimonials
    }
    
    
    return render(request,'index.html',context)


def register(request):
    if request.method =='POST':
        username1=request.POST.get('username')
        password1=request.POST.get('password')
        email1=request.POST.get('email')

        user=User.objects.create_user(
            username=username1,
            password=password1,
            email=email1,
            
        )
        user.save()
        return redirect('login')
    return render(request,'register.html')  

    

def login(request):
    if request.method =='POST':
        username1=request.POST.get('username')
        password1=request.POST.get('password')
        user=authenticate(request,username=username1,password=password1)

        if user is not None:
            auth_login(request,user)
            return redirect('index')
    return render(request,'login.html')



def addprofile(request):
    if request.method=='POST':
        name1=request.POST.get('name')
        place1=request.POST.get('place')
        phone1=request.POST.get('pnumber')
        address1=request.POST.get('address')
        image1 = request.FILES.get('image')
        user2=request.user

        var1=Add_profile.objects.create(
            name=name1,
            place=place1,
            phone=phone1,
            address=address1,
            image=image1,
            user=user2,
        )
        var1.save()
        return redirect('view_profile')
    return render(request,'addprofile.html')


def view_profile(request):
    user=request.user
    view=Add_profile.objects.get(user=user)
    context={
        'var1': view
    }
    return render(request,'view_profile.html',context)



def update_profile(request,):
    user=request.user
    update=Add_profile.objects.get(user=user)
    if request.method=='POST':
        if 'image' in request.FILES:
            os.remove(update.image.path)
            update.image=request.FILES['image']
            update.name=request.POST.get('name')    
            update.phone=request.POST.get('pnumber')  
            update.place=request.POST.get('place')
            update.address=request.POST.get('address')
            update.save()
#           messages.success(request,"SUCCESSFULLY UPDATED!!")
            return redirect('view_profile')
    context={
        'update':update
    }
    return render(request,'update_profile.html',context)



def cart_details(request,pk):
    view=Product.objects.get(pk=pk)
    context={
        'view': view
    }
    return render(request,'cart_details.html',context)

@login_required(login_url='login')
def book_now(request,pk):
    equipment=Product.objects.get(pk=pk)
    if request.method == 'POST':
        
        nday = request.POST.get('nday')
        nhour = request.POST.get('nhour')
        ndate = request.POST.get('ndate')
        Proof = request.FILES['Proof']
        var = Rent.objects.create(
            user=request.user,
            equipment=equipment,
            Proof=Proof,
            Hour=nhour,
            Day=nday,
            Date=ndate,
        )
        var.save()
        return redirect('history')
    context={
        'equipment':equipment
    }
    return render(request,'book_now.html',context)


@login_required(login_url='login')
def history(request):
    user1=request.user
    view=Rent.objects.filter(user=user1)
    context={
        'view':view
    }       
    return render(request,'history.html',context)

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('index')


def testi(request):
    if request.method == 'POST':
        text=request.POST.get('text2')
        user=request.user
        add_profile_instance = Add_profile.objects.get(user=user)

        # Create Testi object with the correct Add_profile instance
        Testi.objects.create(text=text, user=add_profile_instance)
        
        return redirect('index')  # Assuming 'index' is the name of your index view or URL
    else:
        return render(request,'index.html') 
 




########################################## END OF USER FUNCTION ###########################################




############################################# ADMIN FUNCTION ##############################################


def admin_index(request):
    return render(request,'admin/admin_index.html')


def admin_login(request):
    if request.method =='POST':
        username1=request.POST.get('username')
        password1=request.POST.get('password')
        user=authenticate(request,username=username1,password=password1)

        if user is not None and user.is_staff:
            auth_login(request,user)
            return redirect('admin_index')
    return render(request,'admin/admin_login.html')


def admin_profile(request):
    return render(request,'admin/admin_profile.html')



def add_equip(request):
    if request.method=='POST':
        name1=request.POST.get('name')
        pday1=request.POST.get('pday')
        phour1=request.POST.get('phour')
        spec1=request.POST.get('spec')
        image1=request.FILES.get('image')
        desc1=request.POST.get('desc')

        var1=Product.objects.create(
            name=name1,
            priceD=pday1,
            priceH=phour1,
            spec=spec1,
            desc=desc1,
            image=image1,    
        )    
        var1.save()
        messages.success(request,"SUCCESSFULLY ADDED")
        return redirect('add_equip')
    return render(request,'admin/add_equip.html')


def view_equip(request):
    view=Product.objects.all()
    context={
        'var1': view
    }
    return render(request,'admin/view_equip.html',context)  


def update_equip(request,pk):
    update=Product.objects.get(pk=pk)
    if request.method=='POST':
        if 'image' in request.FILES:
            os.remove(update.image.path)
            update.image=request.FILES['image']
            update.name=request.POST.get('name')    
            update.priceD=request.POST.get('pday')  
            update.priceH=request.POST.get('phour')
            update.spec=request.POST.get('spec')
            update.desc=request.POST.get('desc')
            update.save()
#           messages.success(request,"SUCCESSFULLY UPDATED!!")
            return redirect('view_equip')
    context={
        'var1':update
    }
    return render(request,'admin/update_equip.html',context)


def delete_equip(request,pk):
    del_equip=Product.objects.get(pk=pk)
    del_equip.delete()
    messages.success(request,"SUCCESSFULLY DELETED")
    return redirect('view_equip')




def history1(request):
    view=Rent.objects.all()
    context={
        'view':view
    } 
    return render(request,'admin/history.html',context)


def status(request,pk):
    update=Rent.objects.get(pk=pk)
    if request.method=='POST':
        update.Status=True
        update.save()
    return redirect('history1')


def admin_logout(request):
    logout(request)
    return redirect('index')


########################################## END OF ADMIN FUNCTION ###########################################
