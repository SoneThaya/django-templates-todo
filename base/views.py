from django.shortcuts import render
from django.http import HttpResponse


def tasksList(request):
    return HttpResponse('to do list')
