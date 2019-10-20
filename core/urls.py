from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_options, name="show_options"),
    path('patient-info/', views.show_options, name="show_options"),
    path('pms/', views.show_pms, name="show_pms"),
    path('pms/new-registration/', views.add_new_patient, name="add_new_patient"),
    path('pms/search', views.search_by_phone, name="search_by_phone"),
    path('ajax/validate_phone/', views.validate_phone, name="validate_phone"),
    path('pms/add_record/<int:pk>', views.add_record, name="add_patient_record"),
    path('pms/view_history/<int:pk>', views.show_history, name="show_history"),
    path('doctor-view/', views.search_by_id, name="search_by_id"),
    path('doctor-view/view_history/<int:pk>', views.show_history, name="show_patient_history"),
    path('doctor-view/add_record/<int:pk>', views.add_record, name="add_patient_record"),
    path('ims/', views.show_ims_functions, name="ims_functions"),
    path('ims/add-stock', views.add_stock, name="add_stock"),
    path('ajax/validate_uvc/', views.validate_uvc, name="validate_uvc"),
    path('ims/list-stock', views.list_stock, name="list_stock"),

    #add-patient-info, #search-existing-patient
]
