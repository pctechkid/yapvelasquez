"""MyDbProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import include
#from django.urls.conf import include
from myapp1 import signupview
from myapp1 import loginview
from myapp1 import registrationview
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

app_name = 'myapp1'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('myapp1.urls')),
    #  path('subject/', include('myapp1.urls')),
     path('courses/', include('myapp1.urls')),
     path('stud/', include('myapp1.urls')),
   
    
   # path('registration', registrationview.RegistrationView.as_view(), name="registrationview_view"),
    # path('delete_event/<event_id>', views.delete_even, name='delete_event')
]

    #Name diriko mukuha sa name para sa link
    #path('reg/', views.reg, name='reg

#urlpatterns += staticfiles_urlpatterns()