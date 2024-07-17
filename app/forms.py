from django import forms
from .models import Character, Documentation

class StudentForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['username', 'notes', 'age', 'school_grade']
        widgets = {
            'age': forms.NumberInput(attrs={'min': 0}),
            'school_grade': forms.NumberInput(attrs={'min': 0}),
        }

class TutorForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['username', 'notes', 'affiliation']

class AnalystForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['username', 'notes', 'affiliation']

class DocumentationForm(forms.ModelForm):
    pdf_file = forms.FileField(required=False)

    class Meta:
        model = Documentation
        fields = ['name', 'notes', 'task_type', 'content_text', 'pdf_file']

    def save(self, commit=True):
        instance = super().save(commit=False)
        pdf_file = self.cleaned_data.get('pdf_file')

        if pdf_file:
            instance.file_format = pdf_file.content_type
            instance.file_data = pdf_file.read()

        if commit:
            instance.save()

        return instance

