# Generated by Django 3.1.7 on 2021-04-13 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0002_auto_20210413_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='neighbourhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbour.neighbourhood'),
        ),
    ]
