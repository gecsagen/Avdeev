# Небольшой сайт на Django

***

## Описание:

Сайт написан в качестве тестового задания к вакансии Python Backend Developer. Приложение позволяет произвести перепись
сотрудников, для того, чтобы определиться с тем, сколько человек являются сотрудниками.

* **Основные сущности (модели):**
    * 1.Сотрудник (Имя, Фамилия, Возраст, Пол, Отдел)
    * 2.Отдел (Название, этаж)
    * 3.Язык программирования (Название)
* **Обрабатывает следующие пути:**
    * '' - главная страница, отображает список добавленных сотрудников
    * 'add/' - страница добавления нового сотрудника
    * 'about/ - страница описания проекта
    * 'code/' - ссылка на github
    * 'contact/' - страница с контактами
    * 'edit/<slug:pk>/' - страница редактирования данных сотрудника
    * 'delete/<slug:pk>/' - страница удаления данных сотрудника

***
<img height="300" src="https://i.ibb.co/ZGmmPHy/1.png" width="450"/>

### Пакеты и файлы:

* **application** - директория соновоного Django приложения
    * **static** - директория для статики приложения
    * **templates** - директория с HTML шаблонами приложения.
    * **admin.py** - файл настройки админки
    * **apps.py** - файл конфигурации приложения
    * **forms.py** - формы проекта
    * **models.py** - модели проекат
    * **tests.py** - тессты проекта
    * **urls.py** - url проекта
    * **utils.py** - дополнительные классы и функции проекта
    * **view.pys** - представления
* **Avdeev** - директория конфигурации проекта
* **templates** - директория с HTML шаблонами проекта.
* **.gitignore** - файл игнорирования для GIT.
* **db.sqlite3** - файл базы данных проекта в формате SQLite3
* **manage.py** - файл управления Django проектом
* **requirements.txt** - файл содержит список внешних зависимостей проекта.