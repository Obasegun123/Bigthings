# Generated by Django 5.0.6 on 2024-06-25 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('temperature', models.FloatField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
