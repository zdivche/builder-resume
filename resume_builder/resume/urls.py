from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('create/', views.PersonalInfoFormView, name='personal_info_form'),
    path('success/', views.SuccessFormView, name='success_form'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('reg-or-log/', views.register_and_login, name='reg_or_log'),
    path('edit/', views.resume_edit, name='resume_edit'),
]
