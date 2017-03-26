# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guru_responde', '0002_pergunta_data_de_fechamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pergunta',
            name='data_de_fechamento',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
