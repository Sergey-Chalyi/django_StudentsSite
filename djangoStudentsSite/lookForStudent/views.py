from contextlib import redirect_stderr

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

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
