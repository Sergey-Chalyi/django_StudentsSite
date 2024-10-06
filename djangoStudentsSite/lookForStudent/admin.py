from django.contrib import admin

from lookForStudent.models import Student, SpecializationCategory

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # для изменения названий полей, нужно при указаниях
    # полей в моделе добавить параметры verbose_name=''

    # какие поля будет видеть админ в таблице
    list_display = ['id', 'name', 'surname', 'age', 'university', 'category', 'is_published']
    # при нажатии на какое поле записи админу будет переходить на вкладку конкретной записи
    list_display_links = ['id', 'name']
    # сортировка
    ordering = ['id']
    # поля, которые будут доступны для редактирования еще при отображении самой таблицы
    list_editable = ['is_published']
    # сколько записей будет отображаться на одной странице
    list_per_page = 5

admin.site.register(SpecializationCategory)