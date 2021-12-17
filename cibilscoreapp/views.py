from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Register
from .forms import LoginForm
from .forms import RegistrationForm
from .forms import CibilForm


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("valid Details")
        return redirect('login')
    else:
        form = RegistrationForm()
        print("Invalid Details")
    return render(request, 'registration.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            un = request.POST.get('username')
            pwd = request.POST.get('password')
            dbuser = Register.objects.filter(username=un, password=pwd)
            if not dbuser:
                return HttpResponse("Login Failed")
            else:
                print("Login success")
                return redirect('cibil')
        else:
            form = LoginForm(request.POST)
            return render(request, 'personal_details', {'form': form})
    else:
        form = LoginForm(request.POST)
        return render(request, 'login.html', {'form': form})


def cibil(request):
    if request.method == 'POST':
        form = CibilForm(request.POST)
        if form.is_valid():
            sal = int(request.POST.get('salary'))
            if sal < 20000:
                cibil_score = 25 * sal / 1000
                Register.objects.filter(salary=sal)
                if cibil_score >= 750:
                    return HttpResponse("your salary is:" + str(
                        sal) + "<br>your cibil score is :" + str(
                        cibil_score) + "<br>you are eligible for loan")
                else:
                    return HttpResponse("your salary is:" + str(
                        sal) + "<br>your cibil score is :" + str(
                        cibil_score) + "<br>you are not eligible for loan")
            elif sal >= 20000:
                cibil_score = 38 * sal / 1000
                return HttpResponse("your salary is:" + str(
                    sal) + "<br>your cibil score is :" + str(
                    cibil_score) + "<br>you are  eligible for loan")

            elif sal > 25000:
                cibil_score = 35 * sal / 1000
                return HttpResponse("your salary is:" + str(
                    sal) + "<br>your cibil score is :" + str(
                    cibil_score) + "<br>you are  eligible for loan")

            elif sal > 30000:
                cibil_score = 26 * sal / 1000
                return HttpResponse("your salary is:" + str(
                    sal) + "<br>your cibil score is :" + str(
                    cibil_score) + "<br>you are  eligible for loan")

            elif sal > 40000:
                cibil_score = 22 * sal / 1000
                return HttpResponse("your salary is:" + str(
                    sal) + "<br>your cibil score is :" + str(
                    cibil_score) + "<br>you are  eligible for loan")

            elif 53000 < sal <= 65000:
                cibil_score = 14 * sal / 1000
                return HttpResponse("your salary is:" + str(
                    sal) + "<br>your cibil score is :" + str(
                    cibil_score) + "<br>you are  eligible for loan")

            elif 65000 < sal <= 80000:
                cibil_score = 12 * sal / 1000
                return HttpResponse("your salary is:" + str(
                    sal) + "<br>your cibil score is :" + str(
                    cibil_score) + "<br>you are eligible for loan")

            elif 90000 < sal <= 110000:
                cibil_score = 8.5 * sal / 1000
                return HttpResponse("your salary is:" + str(
                    sal) + "<br>your cibil score is :" + str(
                    cibil_score) + "<br>you are eligible for loan")

            elif 110000 < sal <= 130000:
                cibil_score = 7.5 * sal / 1000
                return HttpResponse("your salary is:" + str(
                    sal) + "<br>your cibil score is :" + str(
                    cibil_score) + "<br>you are eligible for loan")

            elif 130000 < sal <= 160000:
                cibil_score = 6 * sal / 1000
                return HttpResponse("your salary is:" + str(
                    sal) + "<br>your cibil score is :" + str(
                    cibil_score) + "<br>you are eligible for loan")

            else:
                return HttpResponse("your salary is:" + str(
                    sal) + "<br>your cibil score is :1000<br>you are eligible for loan")

    else:
        form = CibilForm()
        print("Invalid Details")
    return render(request, 'cibil.html', {'form': form})


def home(request):
    return render(request, 'home.html')
