# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guru_responde', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pergunta',
            name='data_de_fechamento',
            field=models.DateTimeField(null=True),
        ),
    ]
