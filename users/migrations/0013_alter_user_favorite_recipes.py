# Generated by Django 4.2.7 on 2023-12-17 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_alter_recipe_difficulty'),
        ('users', '0012_remove_user_birthday_remove_user_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favorite_recipes',
            field=models.ManyToManyField(blank=True, editable=False, to='recipes.recipe'),
        ),
    ]