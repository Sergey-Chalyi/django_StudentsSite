from django import forms
from lookForStudent.models import Student, SpecializationCategory

class StudentForm(forms.Form):
    gender = forms.CharField(
        max_length=1,
        label='Gender',
        widget=forms.TextInput(attrs={'placeholder': 'Enter gender'})
    )

    name = forms.CharField(
        max_length=255,
        label='Name',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'})
    )

    surname = forms.CharField(
        max_length=255,
        label='Surname',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your surname'})
    )

    age = forms.IntegerField(
        label='Age',
        widget=forms.NumberInput(attrs={'placeholder': 'Enter your age'})
    )

    phone = forms.CharField(
        max_length=255,
        label='Phone',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'})
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )

    university = forms.CharField(
        max_length=255,
        label='University',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your university'})
    )

    specialization = forms.CharField(
        max_length=255,
        label='Specialization',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your specialization'})
    )

    category = forms.ModelChoiceField(
        queryset=SpecializationCategory.objects.all(),
        label='Specialization Category',
        empty_label="Select category..."
    )

    degree = forms.CharField(
        max_length=255,
        label='Degree',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your degree'})
    )

    course = forms.IntegerField(
        label='Course',
        widget=forms.NumberInput(attrs={'placeholder': 'Enter your course'})
    )

    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter a brief description'}),
        required=False
    )

    is_published = forms.BooleanField(
        label='Publish your blank',
        initial=True
    )
