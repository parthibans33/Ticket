from django.shortcuts import render,redirect
from django.urls import reverse
from requests import request
from app_final.forms import LoginForm,TicketGenForm
from .models import LoginModel
# from django.contrib import messages,auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.views.generic import FormView
# from django.template.defaulttags import csrf_token
# Create your views here.



def home_page(request):
    return render(request,'app_final/home_page.html')

# @csrf_token
def register(request):
    if request.method =='POST':
        name = request.POST['name']
        email =request.POST['email']
        password = request.POST['pass']
        
        myuser = User.objects.create_user(username=name,email = email,password = password)
        myuser.save()
        
        # return redirect(request,'app_final/login_page.html')
        return redirect('login')

    return render(request,'app_final/register_page.html')
    pass


def login(request):
    # print(request)
    if request.method =="POST":
        # name = request.POST['name']
        Email =request.POST['email']
        Password = request.POST['password']

        user = authenticate(request,username='Parthiban',email = Email,password = Password)
        if user is not None:
            # print('Hai')
            return redirect('ticket')
            # login(request,user)
        else:
            print('Incorrect Credentials')
            # messages.error(request,'Incorrect Credentials')
            return redirect('home')
    return render(request,'app_final/login_page.html')
    pass

def ticket_gen(request):
    print(request)
    if request.method == 'POST':
        ticket = TicketGenForm(request.POST)
        if ticket.is_valid:
            ticket.cleaned_data()
            data = LoginModel.objects.all()
            return render(request,'app_final/index.html',context={'data':data})
    else:
        ticket = TicketGenForm()
    return render(request,'app_final/ticket_form.html',context={'ticket':ticket})
            
    pass


# class TicketGenerate(FormView):



