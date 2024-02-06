# Generated by Django 4.2.7 on 2024-02-06 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('users', '0019_alter_user_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_recipes',
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='users'),
        ),
    ]
