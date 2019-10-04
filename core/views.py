from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PatientForm

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
            patient = form.save(commit=True)
            patient.save()
            return redirect('/')
        else:
            print("Not Valid!")
    else:
        form = PatientForm()
    return render(request, "core/add-patient.html", {'form': form})
