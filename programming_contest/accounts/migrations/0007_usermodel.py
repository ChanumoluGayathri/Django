# Generated by Django 4.1.5 on 2023-01-17 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_userdata_delete_output_part_testcase_tnum_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usermodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filedata', models.TextField(max_length=1000)),
            ],
        ),
    ]
