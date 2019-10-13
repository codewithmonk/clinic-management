from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_options, name="show_options"),
    path('patient-info/', views.show_options, name="show_options"),
    path('pms/', views.show_pms, name="show_pms"),
    path('pms/new-registration/', views.add_new_patient, name="add_new_patient"),
    path('pms/search', views.search, name="search"),
    path('ajax/validate_phone/', views.validate_phone, name="validate_phone"),
    path('pms/add_record/<int:pk>', views.add_record, name="show_history"),
    path('pms/view_history/<int:pk>', views.show_history, name="show_history"),

    #add-patient-info, #search-existing-patient
]