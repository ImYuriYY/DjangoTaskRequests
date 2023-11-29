from django.shortcuts import render
from django.http import HttpResponse

def error(request):
    return HttpResponse(f'К сожалению, произошла ошибка', status=400, reason="Error!")

def index(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    remote_addr = request.META['REMOTE_ADDR']

    return HttpResponse(f'Host: {host}<br>User browser: {user_agent}<br>User IP: {remote_addr}')

def user(request, userLogin="None", nameFolder="No name", idFolder = "No id"):
    return HttpResponse(f'User login: {userLogin}<br>Name folder: {nameFolder}<br>Folder number: {idFolder}')
