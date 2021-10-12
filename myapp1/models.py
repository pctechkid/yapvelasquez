from django.db import models

# Create your models here.

#para sa ni siya sa table

class Student(models.Model):
    idn = models.CharField(max_length = 20)
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    course = models.CharField(max_length = 20)
    address = models.CharField(max_length=50, default='')
    year = models.IntegerField()


class Subject(models.Model):
    subject_id = models.CharField(max_length = 20)
    subject_name = models.CharField(max_length = 30)


class Course(models.Model):
    course_id = models.CharField(max_length = 20)
    course_name = models.CharField(max_length = 20)
    
class Registration(models.Model):
    reg_id = models.IntegerField() #counter
    idn = models.ForeignKey(Student, on_delete = models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete = models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete = models.CASCADE)
 
 #anything na muapply mudunggan ug 002.