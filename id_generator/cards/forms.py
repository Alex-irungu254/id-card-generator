# forms.py
from django import forms
from .models import IDCard

class IDCardForm(forms.ModelForm):
    class Meta:
        model = IDCard
        fields = ['name', 'dob', 'id_number', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter full name',
            }),
            'dob': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full p-3 border border-gray-300 rounded shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
            'id_number': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter ID number',
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded bg-white',
            }),
        }