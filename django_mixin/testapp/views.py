from django.shortcuts import render

# Create your views here.
from .models  import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin

class StudentList(GenericAPIView, ListModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def post(self,request,*agrs,**kwagrs):
        print("-----request------",request.user)
        return self.create(request,*agrs,**kwagrs)
    
    