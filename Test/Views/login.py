from django.shortcuts import render, redirect
from django.views import View
from ..models.student import Student
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

class Login(View):

    def get(self, request):

        return render(request, 'login.html')
    
    def post(self, request):
        error_message = None
        
        email = request.POST.get('email')
        password = request.POST.get('password')


        if email:
            get_student = Student.objects.get(email=email)
          
            if get_student:
                password_auth = check_password(password, get_student.password)
              
                if password_auth:
                    try:
                        request.session['student'] = get_student.id
                        request.session['student_name'] = get_student.fullname
                        student_id = request.session.get('student')

                      
                        return redirect('Instructions')
                     
                    except Exception as e:
                        error_message = f"An error Occured:{e}"
                    
                   
        data={
            'error':error_message,
        }
        return render(request, 'login.html', data)
        
                

