# Generated by Django 3.1.2 on 2020-10-11 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_ss'),
    ]

    operations = [
        migrations.CreateModel(
            name='edit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=250)),
                ('eurl', models.CharField(max_length=50000)),
                ('edow', models.CharField(max_length=50000)),
                ('esize', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=250)),
                ('gurl', models.CharField(max_length=50000)),
                ('gdow', models.CharField(max_length=50000)),
                ('gsize', models.CharField(max_length=250)),
            ],
        ),
    ]
