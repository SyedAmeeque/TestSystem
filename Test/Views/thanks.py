from django.shortcuts import render, redirect
from django.views import View
from ..models.exam import Exam
from ..models.student import Student
from ..models.questions import Questions
from ..models.result import Result

class Thank(View):

    def get(self, request):
        student = request.session.get('student')
        print(student)
        score = 0
        answer_length = []
        questions = None
        grade = None
        if student: 
            get_student = Student.objects.get(id=student)
            get_question = Questions.objects.filter(subject=get_student.course)
            questions = len(get_question)
            
            for que in get_question:
                answer = Exam.objects.filter(student=get_student, question=que, answer_of_student=que.actual_answer)
                answer_length.append(answer)
                if answer:
                    score += 1
           
            
         
            if score >= 10:
                grade = 'Congratulations! You Have Passed This Exam'
            elif score < 10:
                grade = "You Couldn't pass this Exam Try Next Time!"

           
            try:
                save_result = Result.objects.create(student=get_student,score=score,result=grade,attempted_questions=len(answer_length),total_questions=questions)
                del request.session['student']
                del request.session['student_name']
                data={
                'result':score,
                'que':questions,
                'remarks':grade,
                'attempted_questions':len(answer_length),
                }
                return render(request, 'thanks.html', data)
            except Exception as e:
                print(f'An error occured: {e}')

        data={
            'result':score,
            'que':questions,
            'remarks':grade,
            'attempted_questions':len(answer_length),
        }
        return render(request, 'thanks.html', data)

   