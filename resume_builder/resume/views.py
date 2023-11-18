from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .forms import PersonalInfoForm, EducationForm, ExperienceForm
from .models import PersonalInfo, Education, Experience
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import RegisterForm, LoginForm


def home(request):
    return render(request, 'resume/home.html')


@login_required
def resume_edit(request):
    personal_info = PersonalInfo.objects.filter(user=request.user).first()
    education = Education.objects.filter(user=request.user).first()
    experience = Experience.objects.filter(user=request.user).first()

    personal_info_form = PersonalInfoForm(instance=personal_info)
    education_form = EducationForm(instance=education)
    experience_form = ExperienceForm(instance=experience)

    if request.method == 'POST':
        personal_info_form = PersonalInfoForm(request.POST, instance=personal_info)
        education_form = EducationForm(request.POST, instance=education)
        experience_form = ExperienceForm(request.POST, instance=experience)

        if personal_info_form.is_valid() and education_form.is_valid() and experience_form.is_valid():
            personal_info_form.save()
            education_form.save()
            experience_form.save()
            return redirect('success_form')

    context = {
        'personal_info_form': personal_info_form,
        'education_form': education_form,
        'experience_form': experience_form
    }

    return render(request, 'resume/resume_edit.html', context)


def register_and_login(request):
    register_form = RegisterForm(request.POST)
    login_form = LoginForm(request.POST)
    context = {
        'register_form': register_form,
        'login_form': login_form
    }
    return render(request, 'registration/reg_log.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def PersonalInfoFormView(request):
    if not request.user.is_authenticated:
        message = "Для создания резюме нужно зарегистрироваться"
        return render(request, 'home.html', {'message': message})
    if request.method == 'POST':
        personal_info_form = PersonalInfoForm(request.POST)
        education_form = EducationForm(request.POST)
        experience_form = ExperienceForm(request.POST)
        if personal_info_form.is_valid() and education_form.is_valid() and experience_form.is_valid():
            personal_info = personal_info_form.save(commit=False)
            education = education_form.save(commit=False)
            experience = experience_form.save(commit=False)

            personal_info.user = request.user
            education.user = request.user
            experience.user = request.user

            personal_info.save()
            education.save()
            experience.save()

            return redirect('success_form')
    else:
        personal_info_form = PersonalInfoForm()
        education_form = EducationForm()
        experience_form = ExperienceForm()

    return render(request, 'resume/personal_info_form.html',
                  {'personal_info_form': personal_info_form, 'education_form': education_form,
                   'experience_form': experience_form})


@login_required
def SuccessFormView(request):
    personal_info = PersonalInfo.objects.filter(user=request.user)
    education = Education.objects.filter(user=request.user)
    experience = Experience.objects.filter(user=request.user)
    context = {'personal_info': personal_info, 'education': education, 'experience': experience}

    return render(request, 'resume/success_form.html', context)
