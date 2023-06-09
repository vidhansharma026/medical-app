# Generated by Django 4.2 on 2023-06-23 07:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=20)),
                ('specialist', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='doctor_img')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallary_img')),
            ],
        ),
        migrations.CreateModel(
            name='Msgs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('subject', models.CharField(max_length=20)),
                ('msgs', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('mobile', models.BigIntegerField(unique=True, validators=[django.core.validators.RegexValidator('^[0-9]{10}$')])),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('mobile', models.BigIntegerField(validators=[django.core.validators.RegexValidator('^[0-9]{10}$')])),
                ('date', models.DateField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='medical.doctor')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical.doctor')),
            ],
        ),
    ]
