from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student, Grade
from .serializers import StudentSerializer, GradeSerializer

# Create your views here.

class StudentAPI(APIView):

    def get(self, request):
        students = Student.objects.all()
        serilaizer = StudentSerializer(students, many=True)
        return Response(serilaizer.data)
    
   # def get_one(self, request, id):
   #     student = Student.objects.get(id=id)
   #     serilaizer = StudentSerializer(student, many=False)
   #     return Response(serilaizer.data)

    
    def post(self, request):
        serilaizer = StudentSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data, status=200)
        return Response(serilaizer.error, status=400)

    def put(self, request, id):
        student = Student.objects.get(id=id)
        serilaizer = StudentSerializer(student, data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data, status=200)
        return Response(serilaizer.errors, status=400)
    
    def delete(self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=200)

class GradeAPI(APIView):

    def get(self, request):
        grades = Grade.objects.all()
        serializer = GradeSerializer(grades, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    def put(self, request, id):
        grade = Grade.objects.get(id=id)
        serializer = GradeSerializer(grade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        grade = Grade.objects.get(id=id)
        grade.delete()
        return Response(status=200)
