from django.shortcuts import render, redirect, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PatientForm, PatientRecordForm, StockForm
from .models import Patient, CaseSheet, StockManagement, FinanceManagement
from django.http import JsonResponse
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
import datetime
# from django.http import HttpResponse
# from django.views.generic import View
# import datetime
# from .utils import render_to_pdf



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
            patient = form.save()
            return render(request, 'core/registered.html', {'patient': patient})
        else:
            print("Not Valid!")
    else:
        form = PatientForm()
    return render(request, "core/add-patient.html", {'form': form})


@login_required
def add_record(request, pk):
    patient = Patient.objects.filter(pk=pk)[0]
    if request.method == "POST":
        form = PatientRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.patient = patient
            record.save()
            return redirect('/pms')
        else:
            print("Not Valid!")
    else:
        form = PatientRecordForm()
    return render(request, "core/add-record.html", {'form': form})

@login_required
def show_history(request, pk):
    patient = Patient.objects.filter(pk=pk)[0]
    record_list = CaseSheet.objects.filter(patient_id=pk)
    if len(record_list) > 0:
        message = ""
    else:
        message = "No Records found!"
    page = request.GET.get('page', 1)
    paginator = Paginator(record_list, 2)
    try:
        records = paginator.page(page)
    except PageNotAnInteger:
        records = paginator.page(1)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)
    return render(request, 'core/patient-history.html', {'records': records, 'patient': patient, 'message': message})

@login_required
def search_by_phone(request):
    if request.method == "POST":
        phone_number = request.POST.get('patient_phone_number', None)
        if phone_number:
            # patient = get_object_or_404(Patient, phone=phone_number)
            patient = Patient.objects.filter(phone=phone_number)
            # print(patient[0].name)
            if patient:
                print(patient[0].id)
                return render(request, 'core/patient-info.html', {'patient': patient[0]})
            else:
                return render(request, 'core/search-error.html', {})
    return render(request, 'core/search.html', {})

@login_required
def search_by_id(request):
    if request.method == "POST":
        id = request.POST.get('patient_id', None)
        if id:
            # patient = get_object_or_404(Patient, phone=phone_number)
            patient = Patient.objects.filter(id=id)
            # print(patient[0].name)
            if len(patient) > 0:
                print(patient[0].id)
                return render(request, 'core/patient-info.html', {'patient': patient[0]})
            else:
                return render(request, 'core/search-error.html', {})
    return render(request, 'core/id-search.html', {})

@login_required
def get_patient_info(request, pk):
    patient = Patient.objects.filter(pk=pk)
    if len(patient) > 0:
        patient = patient[0]
        print(patient)
        return render(request, 'core/patient-info.html', {'patient': patient[0]})
    else:
        return JsonResponse({"Error": "Something went wrong!"})


def validate_phone(request):
    phone = request.GET.get('phone', None)
    data = {
        "present": Patient.objects.filter(phone__iexact=phone).exists()
    }
    print(data['present'])
    if data["present"]:
        data["error_message"] = "A user is already registered with this number"
    return JsonResponse(data)


@login_required
def add_stock(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save()
            print("Stock Saved!")
            stocks = StockManagement.objects.all()
            page = request.GET.get('page', 1)
            paginator = Paginator(stocks, 10)
            try:
                records = paginator.page(page)
            except PageNotAnInteger:
                records = paginator.page(1)
            except EmptyPage:
                records = paginator.page(paginator.num_pages)
            return render(request, 'core/stock-info.html', {'records': records})
        else:
            print("Not Valid!")
            medicine_name = form.data["medicine_name"]
            stock_quantity = form.data["quantity"]
            # stock_date = form.data["date"]
            stock = StockManagement.objects.filter(medicine_name=medicine_name)
            if len(stock) > 0:
                stock = stock[0]
                stock.quantity += int(stock_quantity)
                stock.save()
                stocks = StockManagement.objects.all()
                page = request.GET.get('page', 1)
                paginator = Paginator(stocks, 10)
                try:
                    records = paginator.page(page)
                except PageNotAnInteger:
                    records = paginator.page(1)
                except EmptyPage:
                    records = paginator.page(paginator.num_pages)
                return render(request, 'core/stock-info.html', {'records': records})
            else:
                print("Failed")
    else:
        form = StockForm()
    return render(request, "core/add-stock.html", {'form': form})


@login_required
def show_ims_functions(request):
    return render(request, 'core/ims.html', {})


def validate_uvc(request):
    medicine_name = request.GET.get('medicine_name', None)
    stock = StockManagement.objects.filter(medicine_name=medicine_name)
    data = dict()
    if len(stock) > 0:
        print("Stock exists!")
        stock = stock[0]
        category = stock.medicine_category
        manufacturer = stock.manufacturer
        price = stock.unit_price
        data['present'] = True
        data['category'] = category
        data['manufacturer'] = manufacturer
        data['price'] = price
    else:
        data['present'] = False
    return JsonResponse(data)


@login_required
def list_stock(request):
    stocks = StockManagement.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(stocks, 10)
    try:
        records = paginator.page(page)
    except PageNotAnInteger:
        records = paginator.page(1)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)
    return render(request, 'core/stock-info.html', {'records': records})


@login_required
def print_display(request, pk):
    patient = Patient.objects.filter(pk=pk)
    if len(patient) > 0:
        patient = patient[0]
        print(patient)
        return render(request, 'core/prescription-sheet.html', {'patient': patient})
    else:
        return JsonResponse({"Error": "Something went wrong!"})


@login_required
def render_search_stock(request):
    if request.method == "POST":
        medicine_name = request.POST.get('medicine_name', None)
        print(medicine_name)
        if medicine_name:
            stock = StockManagement.objects.filter(medicine_name=medicine_name)
            # print(patient[0].name)
            if len(stock) > 0:
                return render(request, 'core/stock.html', {'stock': stock[0]})
            else:
                return render(request, 'core/search-stock.html', {})
    return render(request, 'core/search-stock.html', {})


@login_required
def delete_stock(request, id):
    medicine = StockManagement.objects.filter(id=id)[0]
    medicine.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def render_billing(request):
    return render(request, 'core/billing.html', {})


@login_required
def generate_registration(request):
    return render(request, 'core/registration-bill.html', {})


def get_user_info(request):
    phone = request.GET.get('phone', None)
    patient = Patient.objects.filter(phone=phone)
    data = dict()
    if len(patient) > 0:
        data['present'] = True
        patient = patient[0]
        data['name'] = patient.name
        data['age'] = patient.age
        data['date'] = datetime.datetime.today().date()
    else:
        data['present'] = False
    if data["present"] is False:
        data["error_message"] = "User not found, please search again!"
    return JsonResponse(data)


def add_finance(request):
    phone = request.GET.get('phone', None)
    particular = request.GET.get('particular', None)
    income = request.GET.get('income', 0)
    expense = request.GET.get('expense', 0)
    data = dict()
    if phone and particular and income and expense:
        item = FinanceManagement(
            particular=particular+"_"+str(phone),
            income=int(income),
            expense=int(expense),
        )
        try:
            item.save()
            data['success'] = True
        except:
            data['success'] = False

    else:
        data['success'] = False
    return JsonResponse(data)







