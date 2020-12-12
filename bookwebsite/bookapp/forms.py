from bookapp.models import Books,Publisher
import django.forms as forms
from django.db import models

class BooksForm(forms.ModelForm):
    class Meta:
        model=Books
        fields='__all__'


class PublisherForm(forms.ModelForm):
    class Meta:
        model=Publisher
        fields='__all__'