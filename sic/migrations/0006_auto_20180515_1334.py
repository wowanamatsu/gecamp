# Generated by Django 2.0.3 on 2018-05-15 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sic', '0005_auto_20180515_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Escolaridade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel_escolar', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Escolaridade',
                'db_table': 'escolaridades',
                'verbose_name_plural': 'Escolaridades',
            },
        ),
        migrations.CreateModel(
            name='Profissao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Profissao',
                'db_table': 'profissoes',
                'verbose_name_plural': 'Profissões',
            },
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='escolaridade',
        ),
        migrations.AddField(
            model_name='pais',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nome_da_mae',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Nome da mãe'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nome_do_pai',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Nome do pai'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='profissao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sic.Profissao'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='escolaridade_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sic.Escolaridade'),
        ),
    ]
