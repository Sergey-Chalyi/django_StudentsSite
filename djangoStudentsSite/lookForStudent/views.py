from contextlib import redirect_stderr
from pipes import Template

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required


from lookForStudent.forms import StudentForm
from lookForStudent.models import Student, SpecializationCategory


def look_student_main(request: HttpRequest):
    data = {
        # передается имя поле для связывания foreign key
        'students': Student.published.all().select_related('category'),
        'categories' : SpecializationCategory.objects.all(),
        'cur_category': None
    }
    return render(request, 'lookForStudent/students_all_blanks_block.html', data)


def student_blank(request: HttpRequest, student_slug):
    data = {
        'student' : get_object_or_404(Student, slug = student_slug)
    }
    return render(request, 'lookForStudent/student_page.html', data)


def specialization_category(request: HttpRequest, category_slug):
    category = get_object_or_404(SpecializationCategory, slug=category_slug)
    students = Student.published.filter(category_id=category.pk)
    data = {
        'students': students,
        'categories' : SpecializationCategory.objects.all(),
        'cur_category' : category
    }
    return render(request, 'lookForStudent/students_all_blanks_block.html', data)


class LookForStudentHome(ListView):
    model = Student
    template_name = 'lookForStudent/students_all_blanks_block.html'

    # сюда прописываются только те данные, которые определяются на момент определения класса
    # то есть, если какой-то параметр формируется динамически, то
    # в этот класс отображения нужно добавить метод get_context_data
    def get_context_data(self, **kwargs):
        # Сначала получаем контекст от родительского класса
        context = super().get_context_data(**kwargs)
        # Добавляем дополнительные данные в контекст
        context['students'] = Student.published.all().select_related('category')
        context['categories'] = SpecializationCategory.objects.all()
        context['cur_category'] = None
        return context



class CreateNewBlank(View):
    def get(self, request: HttpRequest):
        form = StudentForm()
        data = {
            'form': form
        }
        return render(request, 'lookForStudent/new_blank.html', data)

    def post(self, request: HttpRequest):
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                Student.objects.create(**form.cleaned_data)
                return redirect('start_main')
            except:
                print('1')
                form.add_error(None, "Mistake when user filled in the form")
        data = {
            'form': form
        }
        return render(request, 'lookForStudent/new_blank.html', data)



# @login_required
def new_blank(request: HttpRequest):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                Student.objects.create(**form.cleaned_data)
                return redirect('start_main')
            except:
                print('1')
                form.add_error(None, "Mistake when user filled in the form")
    else:
        form = StudentForm()

    data = {
        'form' : form
    }
    return render(request, 'lookForStudent/new_blank.html', data)
