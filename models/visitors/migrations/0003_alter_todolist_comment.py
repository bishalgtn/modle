# Generated by Django 5.1.5 on 2025-01-26 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0002_todolist_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='comment',
            field=models.ManyToManyField(blank=True, to='visitors.comment'),
        ),
    ]
