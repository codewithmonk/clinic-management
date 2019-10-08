from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PatientForm
from .models import Patient

# Create your views here.


@login_required
def show_options(request):
    return render(request, 'core/home.html', {})


@login_required
def show_pms(request):
    return render(request, 'core/pms.html', {})


@login_required
def add_new_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print("Not Valid!")
    else:
        form = PatientForm()
    return render(request, "core/add-patient.html", {'form': form})


@login_required
def search(request):
    if request.method == "POST":
        phone_number = request.POST.get('patient_phone_number', None)
        if phone_number:
            # patient = get_object_or_404(Patient, phone=phone_number)
            patient = Patient.objects.filter(phone=phone_number)
            print(patient[0].name)
            if patient:
                return render(request, 'core/patient-info.html', {'patient': patient[0]})
            else:
                return render(request, 'core/search-error.html', {})
    return render(request, 'core/search.html', {})
