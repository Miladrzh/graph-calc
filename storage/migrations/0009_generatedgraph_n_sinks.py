# Generated by Django 2.1.1 on 2021-04-27 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0008_workloadresult_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='generatedgraph',
            name='n_sinks',
            field=models.FloatField(default=-1),
        ),
    ]