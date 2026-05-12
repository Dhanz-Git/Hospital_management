from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor,Patient,Appointments,Billing
from rest_framework.decorators import api_view
from .serializer import DoctorSerializer,PatientSerializer,AppointmentSerializer,BillingSerializer
@api_view(['GET'])
def get_doctor(request):
      doc=request.query_params.get('name')
      spec=request.query_params.get('spec')
      doct= Doctor.objects.all()
      if doc:
        doct=doct.filter(name__iexact=doc) 
      if spec:
        doct=doct.filter(specialization__iexact=spec) 
      serializer = DoctorSerializer(doct,many =True)
      return Response(serializer.data,status=status.HTTP_200_OK)
@api_view(['POST'])
def create_doctor(request):
     serializer = DoctorSerializer(data = request.data)
     if serializer.is_valid():
        serializer.save()
        return Response({'message':'doctor created','data':serializer.data},status=status.HTTP_201_CREATED)
     return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
@api_view(['PUT'])
def update_doctor(request,pk):
     doct=Doctor.objects.get(pk=pk)
     serializer=DoctorSerializer(doct,data=request.data)
     if serializer.is_valid():
      serializer.save()
      return Response({'message': 'doctor updated', 'doctor': serializer.data},status=status.HTTP_201_CREATED)
     return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete_doctor(request,pk):
     doct=Doctor.objects.get(pk=pk)
     doct.delete()
     return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET'])
def get_patient(request):
    pat=Patient.objects,all()
    serializer=PatientSerializer(pat,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
@api_view(['POST'])
def create_patient(request):
     serializer = DoctorSerializer(data = request.data)
     if serializer.is_valid():
        serializer.save()
        return Response({'message':'patient created','data':serializer.data},status=status.HTTP_201_CREATED)
     return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
@api_view(['PUT'])
def update_patient(request,pk):
     pat=Patient.objects.get(pk=pk)
     serializer=PatientSerializer(pat,data=request.data)
     if serializer.is_valid():
      serializer.save()
      return Response({'message': 'patient updated', 'patient': serializer.data},status=status.HTTP_201_CREATED)
     return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete_patient(request,pk):
     pat=Patient.objects.get(pk=pk)
     pat.delete()
     return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GEt'])
def get_appointment(request):
    doc=request.query_params.get('docid')
    dates=request.query_params.get('date')
    appoint = Appointments.objects.all()
    if doc:
        appoint=appoint.filter(Doctor_id=doc)   
    if dates:
        appoint=appoint.filter(date=dates)
     
    serializer=AppointmentSerializer(appoint,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
@api_view(['POST'])
def create_appointment(request):
     serializer = AppointmentSerializer(data = request.data)
     if serializer.is_valid():
        serializer.save()
        return Response({'message':'appointment fixed','data':serializer.data},status=status.HTTP_201_CREATED)
     return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_appointment_id(request,pk):
     appoints=Appointments.objects.get(pk=pk)
     seriailzer=AppointmentSerializer(appoints)
     return Response(seriailzer.data,status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_billing(request):
    bill = Billing.objects.all()
    serializer= BillingSerializer(bill,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
@api_view(['POST'])
def create_billing(request):
     serializer = BillingSerializer(data = request.data)
     if serializer.is_valid():
        serializer.save()
        return Response({'message':'payment accepted','data':serializer.data},status=status.HTTP_202_ACCEPTED)
     return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
