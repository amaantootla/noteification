# Generated by Django 5.0.7 on 2024-08-31 21:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_folder_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='app.folder'),
        ),
    ]
