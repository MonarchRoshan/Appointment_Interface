# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit_appointment/', views.appointment_form, name='submit_appointment'),
    path('doctorview/', views.doctor_view, name='doctor_view'),
    path('patientview/', views.patient_view, name='patient_view'),
    path('my-view/', views.my_view, name='my_view'),
]
