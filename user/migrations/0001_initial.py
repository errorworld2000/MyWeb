# Generated by Django 3.1.4 on 2020-12-16 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=255)),
                ('user_mail', models.CharField(default='', max_length=50)),
                ('user_status', models.IntegerField()),
            ],
        ),
    ]
