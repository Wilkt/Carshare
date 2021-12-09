from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from carshare.models import Newuser, Payment, Driver
# Create your views here.

def home(request):
    return render(request, 'home.html')

def registration(request):
    if request.method=='POST':
        FName=request.POST.get('FName')
        LName=request.POST.get('LName')
        Email=request.POST.get('Email')
        Residence=request.POST.get('Residence')
        Pwd=request.POST.get('Pwd')
        RPwd=request.POST.get('RPwd')
        Title=request.POST.get('Title')
        #request.session["name"] = FName
        Newuser(FName=FName,LName=LName,Residence=Residence,Email=Email,Pwd=Pwd,RPwd=RPwd,Title=Title).save()
        #messages.success(request, 'Congratulations'+request.POST['FName']+"Account created successfully..!")
        return render(request, 'login.html', {"name": request.session["name"]})
    else:
       return render(request, 'registration.html', {"name": "User"})

def review(request):
    return render(request, 'review.html')

def payment(request):
    if request.method=='POST':
        CName=request.POST.get('CName')
        CNum=int(request.POST.get('CNum'))
        Expm=int(request.POST.get('Expm'))
        Expy=int(request.POST.get('Expy'))
        CVV=int(request.POST.get('CVV'))
        Tbill=int(request.POST.get('Tbill'))
        Payment(CName=CName,CNum=CNum,Expm=Expm,Expy=Expy,CVV=CVV,Tbill=Tbill).save()
        return render(request, 'review.html')

    else:
        return render(request, 'payment.html')

def select(request):
    return render(request, 'select.html')

def signupdriver(request):
    if request.method=='POST':
        Firstname=request.POST.get('Firstname')
        Lastname=request.POST.get('Lastname')
        Residence=request.POST.get('Residence')
        Email=request.POST.get('Email')
        Pass=request.POST.get('Pass')
        Repass=request.POST.get('Repass')
        request.session["name"] = Firstname
        Driver(Firstname=Firstname,Lastname=Lastname,Residence=Residence,Email=Email,Pass=Pass,Repass=Repass).save()
        return render(request, 'login.html', {"name": request.session["name"]})

    else:
        return render(request, 'signupdriver.html', {"name": "User"})

def location(request):
    return render(request, 'location.html')

def login(request):
    if request.method=='POST':
        try:
            Userdetails=Newuser.objects.get(Email=request.POST['Email'], Pwd=request.POST['Pwd'])
            print("Username=",Userdetails)
            request.session['Email'] = Userdetails.Email
            return render(request, 'home.html', {"Email": request.session["Email"]})
        except Newuser.DoesNotExist as e:
            messages.success(request,'Username/Password Invalid..!')
    return render(request,'login.html', {"name": "User"})


def logdriver(request):
    if request.method=='POST':
        try:
            Userdetails=Driver.objects.get(Email=request.POST['Email'], Pass=request.POST['Pass'])
            print("Username=",Userdetails)
            request.session['Email'] = Userdetails.Email
            return render(request, 'home.html', {"Email": request.session["Email"]})
        except Newuser.DoesNotExist as e:
            messages.success(request,'Username/Password Invalid..!')
    return render(request,'logdriver.html', {"name": "User"})    
