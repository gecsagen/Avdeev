from django.urls import path

from application.views import ApplicationHome, AddPage, Contact, Code, About, Edit, Delete

urlpatterns = [
    path('', ApplicationHome.as_view(), name='home'),
    path('add/', AddPage.as_view(), name='add'),
    path('about/', About.as_view(), name='about'),
    path('code/', Code.as_view(), name='code'),
    path('contact/', Contact.as_view(), name='contact'),
    path('edit/<slug:pk>/', Edit.as_view(), name='edit'),
    path('delete/<slug:pk>/', Delete.as_view(), name='delete'),
]
