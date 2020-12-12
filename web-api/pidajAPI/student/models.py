from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    index_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return self.index_number + " " + self.first_name + " " + self.last_name

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.CharField(max_length=20)
    value = models.IntegerField()

    def __str__(self):
        return str(self.student) + " " + self.course + " " + str(self.value)
