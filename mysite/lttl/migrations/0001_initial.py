# Generated by Django 3.1 on 2020-09-04 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('serial_number', models.CharField(max_length=200)),
                ('other_number', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('entity', models.CharField(max_length=200)),
            ],
        ),
    ]
