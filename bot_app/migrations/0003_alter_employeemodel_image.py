# Generated by Django 5.0.2 on 2024-03-03 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_app', '0002_alter_employeemodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='image',
            field=models.ImageField(default='images/person.jpg', upload_to=''),
        ),
    ]
