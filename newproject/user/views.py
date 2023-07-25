from django.shortcuts import render,redirect,get_object_or_404
from.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
import time


# Create your views here.
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        context = {}

        if user is not None:
            login(request, user)
            messages.success(request, 'Hoşgeldin '+ user.username + '!')
            return redirect('index')
        else:
            messages.warning(request, 'Kullanıcı adı veya şifre yanlış!!')
            time.sleep(3)
            return redirect("login")

    context = {}

    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect("login")

def registerPage(request):

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 == password2:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(
                        username=username, email=email, password=password1)

                    userinfo = UserInfo(user=user)
                    userinfo.save()
                    messages.success(
                        request, 'Kaydınız başarıyla oluşturuldu..')
                    return redirect("login")
                else:
                    messages.warning(request, 'Bu mail zaten kullanılıyor!!')
                    return redirect("login")
            else:
                messages.warning(
                    request, 'Bu kullanıcı adı daha önceden alınmış!!')
                return redirect("login")
        else:
            messages.warning(request, 'Şifreler aynı değil!!')
            return redirect("register")

    context = {}

    if request.user.is_authenticated:
        return redirect("index")
    return render(request, 'register.html', context)

def profilePage(request):
    profile = UserInfo.objects.filter(user=request.user)
    user = User.objects.get(username=request.user)

    if request.method == "POST":
        submit = request.POST.get("submit")
        if submit == "profileUpdate":
            fname = request.POST.get("name")
            lname = request.POST.get("surname")
            email = request.POST.get("email")
            username = request.POST.get("username")

            user.first_name = fname
            user.last_name = lname
            user.email = email
            
            if not User.objects.filter(username=username).exists():
                user.username = username
                messages.success(
                    request, "Kullanıcı adınız başarıyla değiştirildi..")
            else:
                messages.warning(
                    request, "Bu kullanıcı adı zaten kullanılıyor!")
        if submit == "passwordChange":
            password = request.POST.get("password")
            if user.check_password(password):  # şifre kontrolü
                password1 = request.POST.get("password1")
                password2 = request.POST.get("password2")
                if password1 == password2:
                    user.set_password(password1)  # şifre değiştirme
                    profile.password = password1
                    login(request, user)
                    messages.success(
                        request, "Şifreniz başarıyla değiştirildi..")
                else:
                    messages.warning(request, "Şifreler eşleşmiyor!")
            else:
                messages.warning(request, "Şifreniz yanlış!")

            profile.save()
        user.save()
        return redirect('profile')

    context = {
        "profile": profile,
        "user": user,
    }

    return render(request, 'profile.html', context)
