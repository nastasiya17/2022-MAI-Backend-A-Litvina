# Generated by Django 3.2.13 on 2022-06-03 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showplace', '0002_auto_20220602_1100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='showplace',
            old_name='sh_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='showplace',
            old_name='sh_name',
            new_name='name',
        ),
    ]
