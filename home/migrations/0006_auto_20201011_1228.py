# Generated by Django 3.1.2 on 2020-10-11 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20201011_1224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='edit',
            old_name='edow',
            new_name='appdow',
        ),
        migrations.RenameField(
            model_name='edit',
            old_name='ename',
            new_name='appname',
        ),
        migrations.RenameField(
            model_name='edit',
            old_name='esize',
            new_name='appsize',
        ),
        migrations.RenameField(
            model_name='edit',
            old_name='eurl',
            new_name='appurl',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='gdow',
            new_name='appdow',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='gname',
            new_name='appname',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='gsize',
            new_name='appsize',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='gurl',
            new_name='appurl',
        ),
        migrations.RenameField(
            model_name='re',
            old_name='mname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='ss',
            old_name='ssdow',
            new_name='appdow',
        ),
        migrations.RenameField(
            model_name='ss',
            old_name='ssname',
            new_name='appname',
        ),
        migrations.RenameField(
            model_name='ss',
            old_name='sssize',
            new_name='appsize',
        ),
        migrations.RenameField(
            model_name='ss',
            old_name='ssurl',
            new_name='appurl',
        ),
    ]
