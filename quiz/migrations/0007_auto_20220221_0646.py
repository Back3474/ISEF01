# Generated by Django 3.2 on 2022-02-21 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_ergebnis'),
    ]

    operations = [
        migrations.AddField(
            model_name='frage',
            name='freigegeben',
            field=models.BooleanField(default=False, help_text='Frage freigeben?', verbose_name='Frage freigeben'),
        ),
        migrations.AddField(
            model_name='richtigoderfalsch',
            name='freigegeben',
            field=models.BooleanField(default=False, help_text='Frage freigeben?', verbose_name='Frage freigeben'),
        ),
        migrations.AlterField(
            model_name='richtigoderfalsch',
            name='behauptungrichtig',
            field=models.BooleanField(default=False, verbose_name='Behauptung wahr?'),
        ),
    ]
