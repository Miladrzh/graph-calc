# Generated by Django 2.1.1 on 2021-04-28 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0011_workloadresult_n_sinks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workloadresult',
            old_name='duration',
            new_name='mean_duration',
        ),
        migrations.AddField(
            model_name='workloadresult',
            name='std_duration',
            field=models.FloatField(default=-1),
        ),
    ]
