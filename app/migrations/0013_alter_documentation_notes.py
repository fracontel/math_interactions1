# Generated by Django 5.0.6 on 2024-07-17 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_model_premis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentation',
            name='notes',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
