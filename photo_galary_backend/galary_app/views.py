from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from galary_app.serializers import *
from .models import *
from django.db.models import Q

@csrf_exempt
def Photo_Add(request):
    if request.method == 'POST':
        received_data = json.loads(request.body)
        print(received_data)
        serializer_check = GalarySerializers(data=received_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"Photo Added Successfully"}))
        else:
            return HttpResponse(json.dumps({"status":"Something Went Wrong"}))
            

@csrf_exempt
def View_Photos(request):
    if request.method == 'POST':
        photoList = AddPhoto.objects.all()
        serialize_data = GalarySerializers(photoList,many=True)
        return HttpResponse(json.dumps(serialize_data.data))
    
    
@csrf_exempt
def Login(request):
    if request.method == 'POST':
        received_data = json.loads(request.body)
        getEmail = received_data["email"]
        getPassword = received_data["password"]
        data = list(User.objects.filter(Q(email__exact=getEmail) & Q(password__exact=getPassword)).values())
        return HttpResponse(json.dumps(data))
    

@csrf_exempt
def Registration(request):
    if request.method == 'POST':
        received_data = json.loads(request.body)
        print(received_data)
        serializer_check = RegistrationSerializers(data=received_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"success"}))
        else:
            return HttpResponse(json.dumps({"status":"something went wrong"}))


@csrf_exempt
def ViewMyPhoto(request):
    if request.method == 'POST':
        received_data = json.loads(request.body)
        getUserid=received_data["user_id"]
        data=list(AddPhoto.objects.filter(user_id=getUserid).values())
        return HttpResponse(json.dumps(data))

