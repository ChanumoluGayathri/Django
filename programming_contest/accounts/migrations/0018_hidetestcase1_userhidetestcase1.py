# Generated by Django 4.1.5 on 2023-02-04 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_finishtime_hometime_logintime_testtime_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HideTestcase1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tnum', models.IntegerField(default=0)),
                ('input', models.CharField(max_length=100)),
                ('output', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserHideTestcase1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tnum', models.IntegerField(default=0)),
                ('input', models.CharField(max_length=100)),
                ('output', models.TextField(max_length=100)),
            ],
        ),
    ]
