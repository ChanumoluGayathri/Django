# Generated by Django 4.1.5 on 2023-01-24 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_userdata_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='score',
            field=models.IntegerField(default=-1),
        ),
    ]
