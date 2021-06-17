from django.shortcuts import render
from app1.seriallizers import *
from app1.models import *
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets


from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from app1.custompermission import mypermission


# Create your views here.

# Function base view
#@csrf_exempt
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_view(self,request,*args,**kwargs):
    if request.method=='GET':
        id=self.kwargs.get('id')
        if id is None:
            obj=student_model.objects.all()
            ser=student_serializer(obj,many=True)
            return Response(ser.data)
        else:
            obj=student_model.objects.get(id=id)
            ser=student_serializer(obj)
            return Response(ser.data)


    elif request.method=='POST':
        ser=student_serializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=201)

        return Response(ser.errors,status=400)
    
    elif request.method=='PUT':
        pk=self.kwargs.get('id')
        print('put iid:: ',pk)
        obj=student_model.objects.get(id=pk)
        ser=student_serializer(obj,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'complete updated'})
        return Response(ser.errors)

    elif request.method=='PATCH':
        #id=self.kwargs.get('id')

        obj=student_model.objects.get(id=pk)
        ser=student_serializer(obj,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'partially updated'})
        return Response(ser.errors)

    elif request.method=='DELETE':

        obj=student_model.objects.get(id=pk)
        obj.delete()
        return Response({'msg':'deleted'})

# Class based view
class student_api_view(APIView):
    def get(self,request,*args, **kwargs):
        id = self.kwargs.get('id')

        if id is not None:
            print('gettt')
            obj=student_model.objects.get(id=id)
            ser=student_serializer(obj)
            return Response(ser.data)
        else:
            obj=student_model.objects.all()
            ser=student_serializer(obj,many=True)
            return Response(ser.data)
    
    def post(self,request):

        print('a===',a)
        ser=student_serializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'created'})
        return Response(ser.errors)

    def put(self,request,*args,**kwargs):
        id=self.kwargs.get('id')
        obj=student_model.objects.get(id=id)
        ser=student_serializer(obj,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'complete updated'})
        return Response(ser.errors)


    def patch(self,request,*args,**kwargs):
        id=self.kwargs.get('id')
        obj=student_model.objects.get(id=id)
        ser=student_serializer(obj,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'partially updated'})
        return Response(ser.errors)


    def delete(self,request,*args,**kwargs):
        id=self.kwargs.get('id')
        obj=student_model.objects.get(id=id)
        obj.delete()
        return Response({'msg':'deleted'})
        

class student_viewset(viewsets.ViewSet):
    queryset=student_model.objects.all
    serializer_class=student_serializer
    authentication_class=[SessionAuthentication]
    permission_class=[mypermission]


    def list(self,request):
        obj=student_model.objects.all()
        ser=student_serializer(obj,many=True)
        return Response(ser.data)
    
    def retrieve(self,request,pk=None):
        obj=student_model.objects.get(id=pk)
        ser=student_serializer(obj)
        return Response(ser.data)

    def create(self,request):
        ser=student_serializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'created'})
        return Response(ser.errors)

    def update(self,request,pk=None):
        
        obj=student_model.objects.get(id=pk)
        ser=student_serializer(obj,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'updated'})
        return Response(ser.errors)
    
    def destroy(self,request,pk=None):
        obj=student_model.objects.get(id=pk)
        obj.delete()
        return Response({'msg':'deleted ok'})
'''
    def hello(self,request):
        print('hello     world')
        return Response({'msg':'jello world'})
'''
# model viewset

class student_model_viewset(viewsets.ModelViewSet):
    queryset=student_model.objects.all()
    serializer_class=student_serializer
    #authentication_classes=[BasicAuthentication]
    #permission_classes=[AllowAny]
   
    #authentication_classes=[BasicAuthentication]
    #permission_classes=[IsAuthenticated]
    
    # basic and session authentication is same
    # isauthenticated any login user can do operation like get post delete etc.
    # isadmin only admin can do operations.
    
    # customer permission

    authentication_classes=[SessionAuthentication]
    permission_classes=[mypermission]
     

# read only model viewset

class student_readonly_modelviewset(viewsets.ReadOnlyModelViewSet):
    queryset=student_model.objects.all()
    serializer_class=student_serializer

