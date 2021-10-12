from django import forms
#from django.db.models import fields
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
     
        fields= '__all__'
       
class CoursesForm(forms.ModelForm):
	
	class Meta:
		model = Course
		fields = '__all__'
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('__all__')   
