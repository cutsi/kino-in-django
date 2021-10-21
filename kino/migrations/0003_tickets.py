# Generated by Django 3.1.5 on 2021-01-11 02:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kino', '0002_karta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('broj_sjedala', models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3')], default='NONE', max_length=10)),
                ('projekcija', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kino.projekcija')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
