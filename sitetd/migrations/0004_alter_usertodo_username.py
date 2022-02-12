# Generated by Django 4.0.1 on 2022-02-07 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sitetd', '0003_alter_usertodo_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertodo',
            name='username',
            field=models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, related_name='userToDo', to=settings.AUTH_USER_MODEL),
        ),
    ]
