from django.contrib import admin

from lookForStudent.models import Student, SpecializationCategory
from django.contrib.admin import SimpleListFilter


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # для изменения названий полей, нужно при указаниях
    # полей в моделе добавить параметры verbose_name=''

    # какие поля будет видеть админ в таблице
    list_display = ['id', 'name', 'surname', 'age', 'university', 'category', 'is_published', 'brief_info']
    # при нажатии на какое поле записи админу будет переходить на вкладку конкретной записи
    list_display_links = ['id', 'name']
    # сортировка
    ordering = ['id']
    # поля, которые будут доступны для редактирования еще при отображении самой таблицы
    # list_editable = ['is_published']
    # сколько записей будет отображаться на одной странице
    list_per_page = 10

    # для добавления пользовательского поля (его нету в бд, только в админке будет отображаться)
    # не забываем в отображаемы е поля добавить 'brief_info'
    # сортировки по данному полю быть не может, ибо это пользовательское поле, поэтому для сортировки
    # это поле нужно связать с существующим
    @admin.display(description='Description length', ordering='name')
    def brief_info(self, student: Student):
        return f"Description length {len(student.description)}"

    # при выделении нескольких полей, с ними можно по умолчанию сделать только удаление
    # для добавления новых действий нужно
    actions = ['set_published', 'set_draft']
    @admin.action(description="Publish chosen blanks")
    def set_published(self, request, queryset):
        # само действие
        count = queryset.update(is_published = Student.Status.PUBLISHED)
        # текст, который будет выводиться после применения данного действия
        self.message_user(request, f'{count} blanks were updated')

    @admin.action(description="Deactivate chosen blanks")
    def set_draft(self, request, queryset):
        # само действие
        count = queryset.update(is_published=Student.Status.DRAFT)
        # текст, который будет выводиться после применения данного действия
        self.message_user(request, f'{count} blanks were deactivated')

    # поле для поиска, тут можно прописывать люкапы
    search_fields = ['name', 'category__name']

    # добавляем фильтры
    list_filter = ['name', 'category__name']

    # включает поля, которые будут видны в просмотре конкретной записи
    fields = ['name']

    # ИСКЛЮЧАЕТ поля, которые НЕ будут видны в просмотре конкретной записи
    # exclude = ['surname']

    # поля, которые будут отображены только для чтения
    readonly_fields = ['created_time']
admin.site.register(SpecializationCategory)