# Generated by Django 4.2.7 on 2024-01-21 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_alter_user_created_recipes_and_more'),
        ('recipes', '0020_alter_recipe_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='creator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='users.user'),
        ),
    ]
