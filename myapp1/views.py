from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import(get_object_or_404,render,HttpResponseRedirect)
from .forms import *


# Create your views here.

class fromroottostudent(View):
    def get(self,request):
        return redirect('myapp1:studenttoindex')

class fromstudenttoindex(View):
    def get(self,request):
        return redirect('myapp1:student_index_view')

class MyIndexView(View):
    def get(self, request):
            return render(request,'index.html')

class DashboardView(View):
    def get(self, request):
        students = Student.objects.all()
        courses = Course.objects.all()
        subjects = Subject.objects.all()
        registration = Registration.objects.all()
        context = {
            'students' : students, #name that we want to use
            'courses' : courses,
            'subjects' : subjects,
            'registration' : registration
        }
        return render(request,'dashboard.html', context)

    def post(self, request):
        if request.method == 'POST':
            if 'btnUpdate' in request.POST:
                print('update button clicked')
                subjectid = request.POST.get("subject-id")
                subjectname = request.POST.get("subject-name")
                update_subject = Subject.objects.filter(subject_id=subjectid).update(subject_name = subjectname)
                print(update_subject)
                print('subject updated')

            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                subjectid = request.POST.get("ssubject-id")
                subjects = Subject.objects.filter(subject_id=subjectid).delete()
                print('recorded deleted')

            elif 'Btnupdate' in request.POST:
                print('update button clicked')
                global Course
                courseid = request.POST.get("course-id")
                coursename = request.POST.get("course-name")
                update_course = Course.objects.filter(course_id=courseid).update(course_name = coursename)
                print(update_course)
                print('course updated')

            elif 'Btndelete' in request.POST:
                print('delete button clicked')
                courseid = request.POST.get("ccourse-id")
                courses = Course.objects.filter(course_id=courseid).delete()
                print('recorded deleted')

            elif 'BtnUpdate' in request.POST:
                print('update button clicked')
                fname = request.POST.get("first-name")
                lname = request.POST.get("last-name")
                Address = request.POST.get("address-address")
                Idn = request.POST.get("idn-idn")                                                                                                                                                                                                                                                                                                                                            
                course = request.POST.get("course-course")
                Year = request.POST.get("year-year")
                update_student = Student.objects.filter(idn=Idn).update(firstname = fname, lastname = lname, course=course, year=Year, address = Address, )
                print(update_student)
                print('student updated')

            elif 'BtnDelete' in request.POST:
                print('delete button clicked')
                Idn = request.POST.get("iidn-idn")
                students = Student.objects.filter(idn=Idn).delete()
                print('recorded deleted')


        return redirect('myapp1:dashboard_view')


    #  def search(request):
 
    # Student = StudentForm.objects.filter(Q(firstname=request.GET.get('search')) | Q(lastname=request.GET.get('search')))
    
    # return render(request, 'dashboard.html', {'members                                                       ': members})       

class SubjectView(View):
    def get(self, request):
        return render(request, 'subject.html')                      
    def post(self, request):
        form = SubjectForm(request.POST)
        if form.is_valid():
            subjectid = request.POST.get("subject_id")
            subjectname = request.POST.get("subject_name")

            form = Subject(subject_id = subjectid, subject_name = subjectname)
            form.save()

            return redirect('myapp1:dashboard_view')

        else:
            print(form.errors)
            return HttpResponse('not valid')


class CourseView(View):
    def get(self, request):
        return render(request, 'courses.html')

    def post(self, request):
        form = CoursesForm(request.POST)
        if form.is_valid():
            courseid = request.POST.get("course_id")
            coursesname = request.POST.get("course_name")

            form = Course(course_id = courseid, course_name = coursesname)
            form.save()

            return redirect('myapp1:dashboard_view')

        else:
            print(form.errors)
            return HttpResponse('not valid')          

class StudentRegistrationView(View):
    # def get(self, request):
    #     return render(request, 'student.html')

    # def post(self, request):
    #     form = StudentForm(request.POST)
    #     if form.is_valid():
    #         studentid = request.POST.get("course_id")
    #         coursesname = request.POST.get("course_name")

    #         form = Course(course_id = courseid, course_name = coursesname)
    #         form.save()

    #         return redirect('myapp1:dashboard_view')

    #     else:
    #         print(form.errors)
    #         return HttpResponse('not valid')

	def get(self, request):
		return render(request, 'student.html')

	def post(self, request):		
		form = StudentForm(request.POST)		
		# fname = request.POST.get("firstname")
		# print(fname)
		# lname = request.POST.get("lastname")
		# print(lname)
		if form.is_valid():
			# try:
            
			fname = request.POST.get("firstname")
			lname = request.POST.get("lastname")
			Address = request.POST.get("address")
			Idn = request.POST.get("idn")
			course = request.POST.get("course")
			Year = request.POST.get("year")
			form = Student(firstname = fname, lastname = lname, address = Address,  idn = Idn, course = course, year = Year)
			form.save()	

			#return HttpResponse('Student record saved!')			
			return redirect('myapp1:dashboard_view')
			# except:
			# 	raise Http404
		else:
			print(form.errors)
			return HttpResponse('not valid')

