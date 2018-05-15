# Generated by Django 2.0.3 on 2018-05-15 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sic', '0004_auto_20180515_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='aliado',
        ),
        migrations.AlterField(
            model_name='estado',
            name='nome',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='estado',
            name='sigla',
            field=models.CharField(max_length=5, unique=True),
        ),
        migrations.AlterField(
            model_name='pais',
            name='codigo',
            field=models.CharField(blank=True, max_length=5, null=True, unique=True),
        ),
    ]
