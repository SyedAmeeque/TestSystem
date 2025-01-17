from django.shortcuts import render
from django.views import View
from ..models.student import Student
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

class Logout(View):

    def get(self, request):
        print(request.session.get('student'))
        del request.session['student']
        del request.session['student_name']
        print(request.session.get('student'))
        print(request.session.get('student_name'))

        return render(request, 'login.html')
    
   
                

