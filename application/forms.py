from django import forms
from .models import Employee


class AddEmployeeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'age', 'departament', 'programing_language']
