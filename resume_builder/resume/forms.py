from django import forms
from .models import PersonalInfo, Education, Experience
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import redirect
class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))

    class Meta:
        model = User
        fields = ['username', 'password']

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect('home')

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Пароль',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect('home')


class PersonalInfoForm(forms.ModelForm):
    date_birth = forms.DateField(input_formats=['%d.%m.%Y'])

    class Meta:
        model = PersonalInfo
        fields = ['name', 'surname', 'date_birth', 'email', 'phone']


class EducationForm(forms.ModelForm):
    start_date_univer = forms.DateField(input_formats=['%d.%m.%Y'])
    end_date_univer = forms.DateField(input_formats=['%d.%m.%Y'])

    class Meta:
        model = Education
        fields = ['university', 'degree', 'description', 'start_date_univer', 'end_date_univer', 'language']


class ExperienceForm(forms.ModelForm):
    start_date = forms.DateField(input_formats=['%d.%m.%Y'])
    end_date = forms.DateField(input_formats=['%d.%m.%Y'])

    class Meta:
        model = Experience
        fields = ['company', 'position', 'start_date', 'end_date', 'description']
