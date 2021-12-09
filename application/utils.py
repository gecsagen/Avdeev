menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'О проекте', 'url_name': 'about'},
    {'title': 'Код проекта', 'url_name': 'code'},
    {'title': 'Контакты', 'url_name': 'contact'},
    {'title': 'Добавить', 'url_name': 'add'},
]


class DataMixin:
    """Класс для формирования контекста запроса"""

    def __init__(self):
        self.request = None

    def get_user_context(self, **kwargs):
        """Формирует и возвращает контекст для шаблона"""
        context = kwargs
        user_menu = menu.copy()
        #  убрать пункт меню добавить, если пользователь не авторизован
        if not self.request.user.is_authenticated:
            user_menu.pop(4)
        context['menu'] = user_menu
        return context
