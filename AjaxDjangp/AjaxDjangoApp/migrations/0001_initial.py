# Generated by Django 4.2.1 on 2023-05-28 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AjaxCrud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.IntegerField()),
                ('PhoneNumber', models.CharField(max_length=20)),
            ],
        ),
    ]
