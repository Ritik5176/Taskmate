# Generated by Django 5.0.1 on 2024-01-27 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0002_tasklist_manage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
