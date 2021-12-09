from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DeleteView

from application.forms import AddEmployeeForm
from application.models import Employee
from application.utils import DataMixin


class ApplicationHome(DataMixin, ListView):
    """
    Представление для отображения списка сотрудников
    (главная страница сайта)
    """
    template_name = 'application/index.html'  # путь до шаблона
    context_object_name = 'employees'  # имя контекста

    def get_context_data(self, *, object_list=None, **kwargs):
        """Функция передачи контекста(параметров)"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Сотрудники')
        return context | c_def

    def get_queryset(self):
        """Какие значаниея из БД вернуть"""
        return Employee.objects.all()


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    """Представление для добавления новой статьи на сайт"""
    form_class = AddEmployeeForm
    #  адрес шаблона
    template_name = 'application/add.html'
    #  адрес перенаправления после добавления статьи
    success_url = reverse_lazy('home')
    #  адрес перенаправления для незарегистрированного пользователя
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        """Функция передачи контекста(параметров)"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление сотрудника')
        return context | c_def


class Contact(DataMixin, TemplateView):
    """
    Представление для отображения страницы с контактами
    """
    template_name = 'application/contact.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        """Функция передачи контекста(параметров)"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Контакты')
        return context | c_def


class Code(DataMixin, TemplateView):
    """
    Представление для отображения ссылки на код проекта
    """
    template_name = 'application/code.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        """Функция передачи контекста(параметров)"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Код')
        return context | c_def


class About(DataMixin, TemplateView):
    """
    Представление для отображения страницы с описанием проекта
    """
    template_name = 'application/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        """Функция передачи контекста(параметров)"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='О проекте')
        return context | c_def


class Edit(DataMixin, UpdateView):
    """Представление редактирования информации о сотруднике"""
    model = Employee
    fields = ['first_name', 'last_name', 'age', 'departament', 'programing_language']
    template_name = 'application/edit.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        """Функция передачи контекста(параметров)"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Редактировать')
        return context | c_def


class Delete(DataMixin, DeleteView):
    """Представление для удаление записи о сотруднике"""
    model = Employee
    success_url = reverse_lazy('home')
    template_name = 'application/delete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        """Функция передачи контекста(параметров)"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Удалить запись')
        return context | c_def
