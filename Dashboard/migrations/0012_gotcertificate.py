# Generated by Django 3.1 on 2021-02-16 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Dashboard', '0011_bookmarked'),
    ]

    operations = [
        migrations.CreateModel(
            name='GotCertificate',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('Fullname', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to='certificate/')),
                ('Date', models.CharField(max_length=255)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]