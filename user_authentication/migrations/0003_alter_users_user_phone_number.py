# Generated by Django 3.2.13 on 2022-05-17 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_authentication', '0002_rename_user_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_phone_number',
            field=models.CharField(max_length=10),
        ),
    ]
