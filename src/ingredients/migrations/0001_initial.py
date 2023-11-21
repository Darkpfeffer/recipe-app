# Generated by Django 4.2.7 on 2023-11-18 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('supplier', models.CharField(max_length=120)),
                ('price', models.FloatField()),
                ('price_unit', models.CharField(choices=[('liter', 'Liter'), ('kilogram', 'Kilogram')], default='Kilogram', max_length=8)),
                ('quantity', models.FloatField()),
                ('quantity_unit', models.CharField(choices=[('milliliter', 'Milliliter'), ('gram', 'Gram')], default='Gram', max_length=10)),
            ],
        ),
    ]
