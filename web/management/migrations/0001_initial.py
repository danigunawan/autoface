# Generated by Django 2.2.7 on 2020-03-20 08:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeKeeping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_link', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(120)])),
                ('emo', models.CharField(max_length=50)),
                ('last_checkin', models.DateTimeField()),
                ('last_checkout', models.DateTimeField()),
                ('prob', models.FloatField()),
            ],
        ),
    ]
