from rest_framework import serializers
from .models import Doctor,Patient,Appointments,Billing
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
class AppointmentSerializer(serializers.ModelSerializer):
    Patient=PatientSerializer(read_only=True)
    Doctor=DoctorSerializer(read_only=True)
    class Meta:
        model = Appointments
        fields = '__all__'
class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = '__all__'