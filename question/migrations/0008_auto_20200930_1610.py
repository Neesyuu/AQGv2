# Generated by Django 3.1 on 2020-09-30 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0007_auto_20200930_1609'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allques',
            old_name='time',
            new_name='timeToSolve',
        ),
        migrations.RenameField(
            model_name='chemistryques',
            old_name='time',
            new_name='timeToSolve',
        ),
        migrations.RenameField(
            model_name='englishques',
            old_name='time',
            new_name='timeToSolve',
        ),
        migrations.RenameField(
            model_name='mathques',
            old_name='time',
            new_name='timeToSolve',
        ),
        migrations.RenameField(
            model_name='physicsques',
            old_name='time',
            new_name='timeToSolve',
        ),
    ]
