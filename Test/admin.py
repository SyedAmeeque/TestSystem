from django.contrib import admin
from .models.student import Student
from .models.questions import Questions
from .models.paper_finished import Paper_finish_time
from .models.result import Result
from .models.exam import Exam
from .models.paper import Paper
from .models.subject_category import Subject
# Register your models here.


class studentAdmin(admin.ModelAdmin):
    list_display=('fullname','batch',)

admin.site.register(Student, studentAdmin)

class QuestionsAdmin(admin.ModelAdmin):
    list_display=('question','option_a','option_b','option_c','option_d','subject')

admin.site.register(Questions, QuestionsAdmin)


class Paper_finished_Admin(admin.ModelAdmin):
    list_display=('Date_time','student')

admin.site.register(Paper_finish_time, Paper_finished_Admin)

class PaperAdmin(admin.ModelAdmin):
    list_display=('date_time','counter')

admin.site.register(Paper, PaperAdmin)


class Exam_Admin(admin.ModelAdmin):
    list_display=('student','date_time','question','answer_of_student')

admin.site.register(Exam, Exam_Admin)

class Result_Admin(admin.ModelAdmin):
    list_display=('id','score','student')

admin.site.register(Result, Result_Admin)

class subject_Admin(admin.ModelAdmin):
    list_display=('Subject',)

admin.site.register(Subject, subject_Admin)