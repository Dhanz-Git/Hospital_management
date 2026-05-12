from django.urls import path
from .views import get_doctor,create_doctor,update_doctor,delete_doctor,get_patient,create_patient,update_patient,delete_patient,get_appointment,create_appointment,get_billing,create_billing,get_appointment_id
urlpatterns =[
path('doctor',get_doctor,name='get_doctor'),
path('create',create_doctor,name='create_doctor'),
path('update',update_doctor,name='update_doctor'),
path('doctor/delete/<int:pk>',delete_doctor,name='delete_doctor'),
path('patient',get_patient,name='get_patient'),
path('create',create_patient,name='create_patient'),
path('update',update_patient,name='update_patient'),
path('delete',delete_patient,name='delete_patient'),
path('Appointments',get_appointment,name='get_appointment'),
path('appointments/<int:pk>',get_appointment_id,name='get_appointment'),
path('create',create_appointment,name='create_appointment'),
path('Billing',get_billing,name='get_billing'),
path('create',create_billing,name='create_billing')








]