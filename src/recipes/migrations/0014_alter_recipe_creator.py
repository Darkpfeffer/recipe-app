# Generated by Django 4.2.7 on 2023-12-17 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_user_created_recipes_alter_user_favorite_recipes'),
        ('recipes', '0013_remove_recipe_creator_id_recipe_creator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='creator',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='users.user'),
        ),
    ]