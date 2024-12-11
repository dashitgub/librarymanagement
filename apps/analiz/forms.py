from django import forms
from .models import Library, Category

class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['name', 'description', 'category']

    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Выберите категорию')

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError('Название книги должно содержать не менее 3 символов.')
        return name