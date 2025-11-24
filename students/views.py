from django.shortcuts import render

# Create your views here.
from .seralizers import StudentSerializer 
from .models import Student
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from django.contrib.auth import get_user_model

# Create your views here.
User=get_user_model()

@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
def student_list(request):
    if request.method == "GET" :
        course=Student.objects.all()
        seralizer=StudentSerializer(course, many=True)
        return Response(serializer.data, status=200)

    if request.method == "POST":
        email=request.data.get("email")
        user_email=User.objects.filter(email=email).first()
        if user_email :
            return Response ({"message": "THis email already exit "},status=400)
        seralizer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            contaxt={
                "message":"student added Successfully",
                "data":serializer.data
            }
            return Response(serializer.data ,status=201)
    return Response(serializer.errors ,status=400)


@api_view(["GET","PUT","PATCH","DELETE"])
@permission_classes([IsAuthenticated])
def student_details(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Exception as e :
        return Response({"errors":"Student does not find"})
        
    if request.method=="GET":
        serializer=StudentSerializer(student)
        return Response(serializer.data)
    
    if request.method in ["PUT","PATCH"]:
        serializer=StudentSerializer(student,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=200)
        return Response (serializer.errors , status=400)
    
    if request.method=="DELETE":
        student.delete()
        return Response ({"message":"Student delete successfully"},status=204)   
         
