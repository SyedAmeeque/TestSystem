from django.shortcuts import render, redirect
from django.views import View
from ..models.student import Student
from ..models.subject_category import Subject
from django.contrib.auth.hashers import make_password
# Create your views here.

class Signup(View):

    def get(self, request):
        subject = Subject.objects.all()
        data={
            'subjects':subject,
        }
        return render(request, 'signup.html', data)
    
    def post(self, request):
        error_message = None
        
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        batch = request.POST.get('batch')
        course = request.POST.get('course')
        password = request.POST.get('password')
        # get_subject = None
        

        if len(name) <= 5:
            error_message = "Enter Full Name Please"
        elif len(password) <= 7:
            error_message = "Password must be 8 characters long"    
        else:
            if password:
                hashed_password = make_password(password)
                try:
                    if course:
                        get_subject = Subject.objects.get(id=course) 
                    
                    student = Student.objects.create(fullname=name,email=email,batch=batch,course=get_subject,password=hashed_password)
                    success_message = "Your account Has been created"
                    
                    return redirect('login')
                
                except Exception as e:
                    error_message = f"An error Occured:{e}"
                    data={
                        'error':error_message
                    }
                    return render(request, 'signup.html', data)
        data={
            'error':error_message
        }
        return render(request, 'signup.html', data)
        
                

