from django.contrib import admin
from .models import Employee, Departament, ProgramingLanguage


class EmployeeAdmin(admin.ModelAdmin):
    """Настройки отображения в админке модели Women"""
    #  поля которые отображаются в админке
    list_display = ('id', 'first_name', 'last_name', 'age', 'gender', 'departament', 'programing_language')
    #  поля которые будут ссылками в админке
    list_display_links = ('id',)
    #  возможность искать по этим полям
    search_fields = ('first_name', 'last_name')
    #  возможность менять поля через админку
    list_editable = ('first_name', 'last_name', 'age', 'gender', 'departament', 'programing_language')
    #  возможность фильтровать по полям в админке
    list_filter = ('age', 'gender', 'departament', 'programing_language')


class DepartamentAdmin(admin.ModelAdmin):
    """Настройки отображения в админке модели Департамент"""
    #  поля которые отображаются в админке
    list_display = ('id', 'name', 'floor')
    #  поля которые будут ссылками в админке
    list_display_links = ('id',)
    #  возможность искать по этим полям
    search_fields = ('name',)


class ProgramingLanguageAdmin(admin.ModelAdmin):
    """Настройки отображения в админке модели Язык программирования"""
    #  поля которые отображаются в админке
    list_display = ('id', 'name')
    #  поля которые будут ссылками в админке
    list_display_links = ('id', 'name')
    #  возможность искать по этим полям
    search_fields = ('name',)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Departament, DepartamentAdmin)
admin.site.register(ProgramingLanguage, ProgramingLanguageAdmin)
