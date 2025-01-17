from django.shortcuts import render,redirect
from ..models.paper_finished import Paper_finish_time
from ..models.student import Student

def finish_lock_auth_middleware(get_response):

    def middleware(request):
        student_id = request.session.get('student')
        if student_id:
            student = Student.objects.get(id=student_id)
            check_paper_exists = Paper_finish_time.objects.filter(student=student)
        
            if check_paper_exists:
                return redirect('thanks')
        
                
        response = get_response(request)

        
        return response

    return middleware