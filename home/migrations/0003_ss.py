# Generated by Django 3.1.2 on 2020-10-11 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_allapp'),
    ]

    operations = [
        migrations.CreateModel(
            name='ss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssname', models.CharField(max_length=250)),
                ('ssurl', models.CharField(max_length=50000)),
                ('ssdow', models.CharField(max_length=50000)),
                ('sssize', models.CharField(max_length=250)),
            ],
        ),
    ]