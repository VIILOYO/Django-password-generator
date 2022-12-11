import random

from django.shortcuts import render


def index(request):
    """Форма"""
    context = {'title': 'Генератор паролей',
               'numbers':range(6,15)}
    return render(request, 'generator/index.html', context=context)


def password(request):
    """Получение пароля"""
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!№%?*+~@#$%^&*'))

    password = ''
    for x in range(length):
        password += random.choice(characters)

    context = {'title': 'Пароль',
               'password': password,}
    return render(request, 'generator/password.html', context=context)


def info(request):
    return render(request, 'generator/info.html', {'title': 'Информация'})
