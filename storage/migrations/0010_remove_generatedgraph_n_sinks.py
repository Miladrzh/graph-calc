# Generated by Django 2.1.1 on 2021-04-27 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0009_generatedgraph_n_sinks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generatedgraph',
            name='n_sinks',
        ),
    ]
