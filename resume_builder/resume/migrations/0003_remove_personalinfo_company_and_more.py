# Generated by Django 4.2.5 on 2023-11-04 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resume', '0002_personalinfo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinfo',
            name='company',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='degree',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='description',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='end_date_univer',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='position',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='start_date_univer',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='university',
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='date_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Опыт работы',
                'verbose_name_plural': 'Опыт работы',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=100)),
                ('degree', models.CharField(blank=True, max_length=100, null=True)),
                ('start_date_univer', models.DateField(blank=True, null=True)),
                ('end_date_univer', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Образование',
                'verbose_name_plural': 'Образование',
            },
        ),
    ]
