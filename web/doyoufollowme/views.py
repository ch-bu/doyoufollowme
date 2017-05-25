from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from htmlmin.decorators import minified_response
from django.contrib.auth.decorators import login_required


@minified_response
def index(request):
    # Serve landing page
    return HttpResponse('sasdf')
