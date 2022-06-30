# Generated by Django 4.0.5 on 2022-06-30 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=16)),
                ('lastname', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('password1', models.CharField(max_length=10)),
                ('password2', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'patient_register',
            },
        ),
    ]
