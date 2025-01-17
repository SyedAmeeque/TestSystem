from django.shortcuts import render,redirect
from ..models.paper import Paper
from ..models.student import Student

def start_exam_auth_middleware(get_response):

    def middleware(request):
        student_id = request.session.get('student')
        if student_id:
            student = Student.objects.get(id=student_id)
            check_paper_exists = Paper.objects.filter(student=student)
        
        if not check_paper_exists:
            return redirect('Instructions')
        
                
        response = get_response(request)

        
        return response

    return middleware