# Generated by Django 3.2.13 on 2022-05-18 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_authentication', '0006_auto_20220517_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='company_id',
            new_name='company',
        ),
    ]