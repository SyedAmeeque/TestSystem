from django import template
from ..models.exam import Exam
from ..models.student import Student
from ..models.exam import Exam
from ..models.questions import Questions

register = template.Library()

@register.filter(name="show_answered_question")
def check_answered_question(question, student):
    get_student = Student.objects.get(id=student)
    check_question = Exam.objects.filter(student=get_student,question=question)

    for que in check_question:
        if que.answer_of_student == question.option_a:
            return 1
        elif que.answer_of_student == question.option_b:
            return 2
        elif que.answer_of_student == question.option_c:
            return 3
        elif que.answer_of_student == question.option_d:
            return 4
    
    return 0

@register.filter('is_answer_send')
def is_answer_send(question, student):
    get_student = Student.objects.get(id=student)
    check_question = Exam.objects.filter(student=get_student,question=question)
    for a in check_question:
        if a :
            return True
    return False



@register.filter('answers_count')
def answers_count(student):
    get_student = Student.objects.get(id=student)
    check_question = Exam.objects.filter(student=get_student)
    total = len(check_question)

    return total


@register.filter('get_question_number')
def get_question_number(que,student):
    get_student = Student.objects.get(id=student)
    questions = Questions.objects.filter(subject=get_student.course)
    
    for q in questions:
        if q == que: 
            index = questions.index(q)
            print(index)
            return index+1

    return 0 
