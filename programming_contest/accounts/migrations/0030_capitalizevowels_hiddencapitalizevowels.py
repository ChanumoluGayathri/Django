# Generated by Django 4.1.5 on 2023-02-07 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_hiddenmagicnum_magicnum'),
    ]

    operations = [
        migrations.CreateModel(
            name='CapitalizeVowels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tnum', models.IntegerField(default=0)),
                ('input', models.CharField(max_length=100)),
                ('output', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HiddenCapitalizeVowels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tnum', models.IntegerField(default=0)),
                ('input', models.CharField(max_length=100)),
                ('output', models.TextField(max_length=100)),
            ],
        ),
    ]
