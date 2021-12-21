from django.db import models
from django.urls import reverse


class Departament(models.Model):
    """Отдел (департамент)"""

    name = models.CharField(max_length=50, verbose_name='Название отдела')
    floor = models.PositiveIntegerField(verbose_name='Этаж')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class ProgramingLanguage(models.Model):
    """Язык программирования"""
    name = models.CharField(max_length=50, verbose_name='Язык программирования(категория)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'


class Employee(models.Model):
    """Сотрудник"""
    first_name = models.CharField(max_length=50, verbose_name='Имя сотрудника')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия сотрудника')
    age = models.PositiveIntegerField(verbose_name='Возраст сотрудника')
    gender = models.CharField(max_length=20, verbose_name='Пол', choices=[('M', 'Мужской'), ('F', 'Женский')],
                              blank=True)
    departament = models.ForeignKey(Departament, blank=False, verbose_name='Департамент', on_delete=models.CASCADE)
    programing_language = models.ForeignKey(ProgramingLanguage, blank=False,
                                            verbose_name='Язык программирования',
                                            on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.last_name} {self.first_name}, департамент: {self.departament}"

    def get_absolute_url(self):
        """Возвращает путь для редактирования записи"""
        return reverse('edit', kwargs={'pk': self.pk})

    def get_delete_url(self):
        """Возвращает путь для удаления записи"""
        return reverse('delete', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'