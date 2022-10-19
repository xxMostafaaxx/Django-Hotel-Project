# Generated by Django 3.1.4 on 2021-02-27 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0022_room_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='image',
        ),
        migrations.AlterField(
            model_name='room',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]