# Generated by Django 3.1 on 2020-11-09 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0002_userdetail_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='glevel',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
