# Generated by Django 2.1.2 on 2018-10-27 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20181027_1617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specialsnake',
            old_name='image',
            new_name='images',
        ),
    ]