# Generated by Django 5.0.2 on 2024-03-03 08:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PositionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('birth_date', models.DateField()),
                ('image', models.ImageField(default='media/person.jpg', upload_to='')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot_app.positionmodel')),
            ],
        ),
    ]
