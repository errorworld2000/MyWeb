# Generated by Django 3.1.4 on 2020-12-15 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_mail',
            field=models.CharField(default='', max_length=50),
        ),
    ]