from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
from django.http import HttpResponse

from .models import Patient


def index(request):
    return redirect('/admin/')
