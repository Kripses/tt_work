# Generated by Django 5.0.2 on 2024-02-27 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='src/uploads/'),
        ),
    ]