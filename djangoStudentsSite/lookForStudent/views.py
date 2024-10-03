from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from lookForStudent.models import Student, SpecializationCategory


def look_student_main(request: HttpRequest):
    data = {
        'students': Student.published.all(),
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