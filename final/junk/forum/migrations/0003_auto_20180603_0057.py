# Generated by Django 2.0.4 on 2018-06-03 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20180602_1907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resposta',
            old_name='topico',
            new_name='topico_fk',
        ),
    ]
