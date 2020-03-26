# Generated by Django 2.2.5 on 2020-03-18 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0002_imagedetail_visited'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagedetail',
            old_name='img_url',
            new_name='file_path',
        ),
        migrations.RemoveField(
            model_name='imagedetail',
            name='tag_name',
        ),
        migrations.RemoveField(
            model_name='imagedetail',
            name='visited',
        ),
        migrations.AddField(
            model_name='imagedetail',
            name='prod1',
            field=models.BooleanField(default=''),
        ),
        migrations.AddField(
            model_name='imagedetail',
            name='prod2',
            field=models.BooleanField(default=''),
        ),
        migrations.AddField(
            model_name='imagedetail',
            name='prod3',
            field=models.BooleanField(default=''),
        ),
        migrations.AddField(
            model_name='imagedetail',
            name='top1',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='imagedetail',
            name='top2',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='imagedetail',
            name='top3',
            field=models.TextField(default=''),
        ),
    ]