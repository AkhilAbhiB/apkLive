# Generated by Django 3.1.2 on 2020-10-11 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='allapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appname', models.CharField(max_length=250)),
                ('appurl', models.CharField(max_length=50000)),
                ('appdow', models.CharField(max_length=50000)),
                ('appsize', models.CharField(max_length=250)),
            ],
        ),
    ]
