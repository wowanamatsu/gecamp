# Generated by Django 2.0.3 on 2018-05-15 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sic', '0006_auto_20180515_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='pais',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
