from django.contrib.auth.models import User
from django.db import models


class PersonalInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_birth = models.DateField(null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Персональная информация'
        verbose_name_plural = 'Персональные данные'

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    university = models.CharField(max_length=100)
    degree = models.CharField(max_length=100, null=True, blank=True)
    start_date_univer = models.DateField(null=True, blank=True)
    end_date_univer = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    language = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return f"{self.degree} at {self.university} ({self.start_date_univer} - {self.end_date_univer})"
    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образование"

class Experience(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        company = models.CharField(max_length=100)
        position = models.CharField(max_length=100)
        start_date = models.DateField()
        end_date = models.DateField(null=True, blank=True)
        description = models.TextField(null=True, blank=True)

        def __str__(self):
            return f"{self.position} в {self.company} ({self.start_date} - {self.end_date})"

        class Meta:
            verbose_name = "Опыт работы"
            verbose_name_plural = "Опыт работы"


