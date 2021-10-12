from django.urls import include, path
from myapp1 import views
from myapp1 import signupview, loginview
#from myapp1 import registrationview
#from myapp1 import dashboardviews


#paths arranged alphabetically by name

app_name= 'myapp1'
urlpatterns= [
    #urls for student app
path('index', views.MyIndexView.as_view(), name="student_index_view"),
    path('dashboard', views.DashboardView.as_view(), name="dashboard_view"),
    path('subject', views.SubjectView.as_view(), name="subject_view"),
    #path('loginpage', views.LogInView.as_view(), name="login_view"),   
    path('courses', views.CourseView.as_view(), name="course_view"), 
    path('students', views.StudentRegistrationView.as_view(), name="student_view"),  
     path('signup', signupview.SignUpView.as_view(), name="signup_view"),
    path('login', loginview.LogInView.as_view(), name="loginview_view"),
    # path('search', views.search, name="search"),
]       


