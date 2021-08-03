# Generated by Django 3.1.7 on 2021-07-31 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simplecourse.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simplecourse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_image',
            field=models.ImageField(upload_to=simplecourse.models.user_directory_path),
        ),
    ]
