from django import forms
from app.models import *
from django.forms import ClearableFileInput

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('email','password', )
        widgets = {
        'password': forms.PasswordInput(),
    }

class DocumentForm2(forms.ModelForm):
    class Meta:
        model = Document2
        fields = ('types','category',)
        widgets = {
        'document_excel': ClearableFileInput(attrs={'multiple': True}),
        'document_pdf': ClearableFileInput(attrs={'multiple': True}),
        }