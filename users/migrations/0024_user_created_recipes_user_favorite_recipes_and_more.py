# Generated by Django 4.2.7 on 2024-02-06 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0022_alter_recipe_creator'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0023_remove_user_favorite_recipes_remove_user_user_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_recipes',
            field=models.ManyToManyField(blank=True, related_name='created_recipes', to='recipes.recipe'),
        ),
        migrations.AddField(
            model_name='user',
            name='favorite_recipes',
            field=models.ManyToManyField(blank=True, related_name='favorite_recipes', to='recipes.recipe'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_info',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
