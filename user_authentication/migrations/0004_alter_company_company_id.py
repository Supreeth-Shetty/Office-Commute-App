# Generated by Django 3.2.13 on 2022-05-17 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_authentication', '0003_alter_users_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.CharField(max_length=10),
        ),
    ]