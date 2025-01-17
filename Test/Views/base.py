from django.shortcuts import render, redirect
from django.views import View
from ..models.student import Student
from ..models.paper import Paper
from Test.middlewares.auth import login_auth_middleware
from Test.middlewares.is_given_paper_auth import paper_auth_middleware
from django.utils.decorators import method_decorator
# Create your views here.

class Base(View):
    
    @method_decorator(login_auth_middleware)
    @method_decorator(paper_auth_middleware)
    def get(self, request):
        student = request.session.get('student')
        if student:
            get_student = Student.objects.get(id=student)
        data={
            'student':get_student,
        }
        return render(request, 'base.html', data)
    
    def post(self, request):

        is_paper_started = request.POST.get('is_paper_started')
        student = request.session.get('student')
        if student:
            get_student = Student.objects.get(id=student)
            if is_paper_started=="on": 
                save_student_started_paper = Paper.objects.create(student=get_student)
                print('yes')
                return redirect('Exam')
            else:
                print('no')
        return render(request, 'base.html')
                

