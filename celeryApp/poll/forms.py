
from django import forms

from poll.models import Calculator


class UserForm(forms.ModelForm):
    class Meta:
        model = Calculator
        fields = [
            "number",
        ]