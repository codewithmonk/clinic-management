from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_options, name="show_options"),
    path('patient-info/', views.show_options, name="show_options"),
    path('pms/', views.show_pms, name="show_pms"),
    path('pms/new-registration/', views.add_new_patient, name="add_new_patient"),
    #add-patient-info, #search-existing-patient
]