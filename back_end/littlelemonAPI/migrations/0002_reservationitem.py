# Generated by Django 5.1.6 on 2025-02-25 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('littlelemonAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('partySize', models.IntegerField()),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
