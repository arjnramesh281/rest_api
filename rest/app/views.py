from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from .models import *
from .serializers import *
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

def sample_fun(req):
    d=rest_user.objects.all()
    s=sample(d,many=True)
    return JsonResponse(s.data,safe=False)

@csrf_exempt

def model_view(req):
    if req.method=='GET':
        d=rest_user.objects.all()
        s=model(d,many=True)
        return JsonResponse(s.data,safe=False)
    elif req.method=='POST':
        d=JSONParser().parse(req)
        s=model(data=d)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data)
        else:
            return JsonResponse(s.errors)
        
@csrf_exempt

def update_view(req,id):
    try:
        demo=rest_user.objects.get(pk=id)
    except:
        return HttpResponse('invalid id')
    if req.method=='GET':
        s=model(demo)
        return JsonResponse(s.data,safe=False)
    elif req.method=='PUT':
        d=JSONParser().parse(req)
        s=model(demo,data=d)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data)
        else:
            return JsonResponse(s.errors)
    elif req.method=='DELETE':
        demo.delete()
        return HttpResponse("deleted")
    
@api_view(['GET','POST'])
def fun1(req):
    if req.method=='GET':
        d=rest_user.objects.all()
        s=model(d,many=True)
        return Response(s.data)
    elif req.method=='POST':
        s=model(data=req.data)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data,status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(s.errors,status=status.HTTP_400_BAD_REQUEST)
        
    
@api_view(['GET','PUT','DELETE'])
def fun2(req,id):
        try:
            demo=rest_user.objects.get(pk=id)
        except:
            return HttpResponse('invalid id')
        if req.method=='GET':
            s=model(demo)
            return Response(s.data)
        elif req.method=='PUT':
            s=model(demo,data=req.data)
            if s.is_valid():
                s.save()
                return JsonResponse(s.data,status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(s.errors,status=status.HTTP_400_BAD_REQUEST)
        elif req.method=='DELETE':
            demo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        