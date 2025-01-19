from django.shortcuts import render, redirect
from django.views import View
from ..models.questions import Questions 
from ..models.student import Student 
from ..models.paper_finished import Paper_finish_time 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Test.middlewares.auth import login_auth_middleware
from Test.middlewares.start_exam_auth import start_exam_auth_middleware
from Test.middlewares.lock_after_finsih import finish_lock_auth_middleware
from django.utils.decorators import method_decorator
from ..models.exam import Exam
from ..models.paper import Paper



class Home(View):
   
    @method_decorator(login_auth_middleware)
    @method_decorator(start_exam_auth_middleware)
    @method_decorator(finish_lock_auth_middleware)
    def get(self, request):
        student = request.session.get('student')
        get_student = Student.objects.get(id=student)
        questions = Questions.objects.filter(subject=get_student.course)
        paginator = Paginator(questions, 1)
        page_number = request.GET.get('page')
        if page_number:
            request.session['page_number'] = page_number

        counter = None
        count=0
        get_count = request.GET.get('count')
        
        if get_count:
            request.session['count_number'] = get_count
            count=get_count
        elif page_number==None:
            count=1
            if request.session.get("count_number"):
                del request.session['count_number']
        else:
            count=page_number
            if request.session.get("count_number"):
                del request.session['count_number']

        print(request.session.get("count_number"))
    
        
        if student:
            try:
                paper = Paper.objects.get(student__id=student)
                print(paper.time_remaining())
                if paper.time_remaining() <= 0:
                    return redirect('thanks')
            except Exception as e:
                print(e)
      
        try:
            page_obj = paginator.page(count)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        print('page_object:', page_obj)


        data={
            'count':count,
            'page_obj':page_obj,
            'mcqs':questions,
            'total_questions':len(questions),
            'counter': paper.time_remaining,
        }        
        return render(request, 'index.html', data)
    
    
    @method_decorator(finish_lock_auth_middleware)
    def post(self, request):
       
    
        question = request.POST.get('question_id')
        answer = request.POST.get('answer')
        student = request.session.get('student')
        page_number= request.session.get("page_number")
        count_number= request.session.get("count_number")
        get_paper = Paper.objects.get(student__id=student)

        if count_number == None:
            count_number = 1
     
        if student and question:
            get_student = Student.objects.get(id=student)
            get_question = Questions.objects.get(id=question)
            if question and answer:
                try:
                    get_answer = Exam.objects.filter(student=get_student,question=get_question).first()
                    if get_answer:
                        get_answer.answer_of_student = answer
                        get_answer.save()
                        save_questions = get_paper.Exams.add(get_answer)
                        get_paper.save()
                        
                        if count_number:
                            return redirect(f'/Exam/?page={page_number}&count={count_number}')
                        else:
                            if count_number:
                                del request.session['count_number']

                            return redirect(f'/Exam/?page={page_number}')
                    else:    
                        save_answer = Exam.objects.create(student=get_student,question=get_question,answer_of_student=answer)
                        save_questions = get_paper.Exams.add(save_answer)
                        get_paper.save()
                        if count_number:
                            return redirect(f'/Exam/?page={page_number}&count={count_number}')
                        else:
                            if count_number:
                                del request.session['count_number']

                            return redirect(f'/Exam/?page={page_number}')

                except Exception as e:
                    print(f"an error occured: {e}")
                    if count_number:
                        return redirect(f'/Exam/?page={page_number}&count={count_number}')
                    else:
                        if count_number:
                            del request.session['count_number']

                            return redirect(f'/Exam/?page={page_number}')
        
        is_paper_finish = request.POST.get('is_paper_finish')
        if is_paper_finish:
            if student:
                get_student = Student.objects.get(id=student)
                if is_paper_finish == "on":
                    complete = Paper_finish_time.objects.create(student=get_student)
                    return redirect('thanks')

     
                

