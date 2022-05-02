from django.shortcuts import render


def home(req):
    context = {"title": 'home'}
    return render(req, 'base/index.html', context)


def agency(req):
    context = {"title": 'agency'}
    return render(req, 'base/agency.html', context)
