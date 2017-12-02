from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
from django.http import HttpResponse

from .models import Patient


def index(request):
    return redirect('/admin/')

def detail(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, 'registrations/detail.html', {'patient': patient})

def results(request, patient_id):
    response = "You're looking at the results of patient %s."
    return HttpResponse(response % patient_id)

def update(request, patient_id):
    return HttpResponse("You're updating patient %s." % patient_id)
