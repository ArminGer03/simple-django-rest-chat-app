# Generated by Django 4.2.5 on 2023-10-11 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatter', '0003_alter_message_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
