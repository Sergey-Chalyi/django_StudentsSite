from django.contrib import admin

from lookForJob.models import Job

class JobAdmin(admin.ModelAdmin):
    # для изменения названий полей, нужно при указаниях полей в моделе добавить параметры verbose_name=''

    # какие поля будет видеть админ в таблице
    list_display = ['id', 'company', 'title', 'salary']
    # при нажатии на какое поле записи админу будет переходить на вкладку конкретной записи
    list_display_links = ['id', 'company']
    # сортировка
    ordering = ['id']

admin.site.register(Job, JobAdmin) # или можно использовать как декоратор с первым параметром Job

