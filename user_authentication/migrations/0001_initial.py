# Generated by Django 3.2.13 on 2022-05-15 06:08

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_id', models.IntegerField()),
                ('branch_address', models.TextField()),
                ('created_date', models.DateField()),
                ('updated_date', models.DateField()),
                ('branch_status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.IntegerField()),
                ('company_name', models.CharField(max_length=100)),
                ('created_date', models.DateField()),
                ('updated_date', models.DateField()),
                ('company_status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usertype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usertype_id', models.IntegerField()),
                ('usertype', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('updated_date', models.DateField()),
                ('admin_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=100)),
                ('user_phone_number', phone_field.models.PhoneField(help_text='Contact number', max_length=31)),
                ('user_email_id', models.EmailField(blank=True, max_length=254, unique=True)),
                ('user_password', models.CharField(max_length=100)),
                ('created_date', models.DateField()),
                ('updated_date', models.DateField()),
                ('user_status', models.CharField(max_length=10)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_authentication.branch')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_authentication.company')),
                ('user_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_authentication.usertype')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_1', models.TextField()),
                ('location_2', models.TextField()),
                ('created_date', models.DateField()),
                ('updated_date', models.DateField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_authentication.user')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='company_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_authentication.company'),
        ),
    ]