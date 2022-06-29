from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Login')
            return redirect('login')

    return render(request, 'login.html')


def sign(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phonenumber = request.POST['Number']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Exist")
                return redirect('sign')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exist")
                return redirect('sign')
            elif User.objects.filter(last_name=phonenumber).exists():
                messages.info(request, "Mobile Number Already Exist")
                return redirect('sign')
            else:
                user = User.objects.create_user(username=username, email=email, password=password,
                                                last_name=phonenumber)
                user.save()
                return redirect('login')

        else:
            messages.info(request, 'password incorrect')
            return redirect('sign')
        return redirect('/')
    return render(request, "sign.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
