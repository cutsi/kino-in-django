# Generated by Django 3.1.5 on 2021-01-15 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0003_tickets'),
    ]

    operations = [
        migrations.AddField(
            model_name='projekcija',
            name='broj_prodanih_karata',
            field=models.IntegerField(default=0),
        ),
    ]
