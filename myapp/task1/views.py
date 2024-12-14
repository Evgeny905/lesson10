from django.shortcuts import render
from django.http import HttpResponse
from task1.forms import UserRegister
from task1.models import *
def Platform(request):
    return render(request, 'platform.html')
def Games(request):
    return render(request, 'games.html', {'games': Game.objects.all()})
def Cart(request):
    return render(request, 'cart.html')
def sign_up_by_django(request):
    users = Buyer.objects.all()
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])
            for user in users:
                if user.name == username:
                    info['Error']='Пользователь уже существует'
                    return render(request, 'registration_page.html', info)
                else:
                    continue
            if password == repeat_password and age >= 18:
                Buyer.objects.create(name=username, balance="1000", age=age)
                return HttpResponse(f'Приветствуем, {username}!')
            elif password != repeat_password:
                info['Error'] = 'Пароли не совпадают'
                return render(request, 'registration_page.html', info)
            elif age < 18:
                info['Error'] = 'Вы должны быть старше 18'
                return render(request, 'registration_page.html', info)
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {form: 'form'})
def sign_up_by_html(request):
    users = Buyer.objects.all()
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])
            for user in users:
                if user.name == username:
                    info['Error'] = 'Пользователь уже существует'
                    return render(request, 'registration_page.html', info)
                else:
                    continue
            if password == repeat_password and age >= 18:
                Buyer.objects.create(name=username, balance="1000", age=age)
                return HttpResponse(f'Приветствуем, {username}!')
            elif password != repeat_password:
                info['Error'] = 'Пароли не совпадают'
                return render(request, 'registration_page.html', info)
            elif age < 18:
                info['Error'] = 'Вы должны быть старше 18'
                return render(request, 'registration_page.html', info)
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {form: 'form'})