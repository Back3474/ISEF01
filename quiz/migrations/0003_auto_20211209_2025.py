# Generated by Django 3.2 on 2021-12-09 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20211209_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='frage',
            name='antwort1',
            field=models.CharField(help_text='Geben Sie die Antwort1 der Frage ein', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='frage',
            name='antwort1richtig',
            field=models.BooleanField(default=False, help_text='Geben Sie an ob Antwort1 richtig ist'),
        ),
        migrations.AddField(
            model_name='frage',
            name='antwort2',
            field=models.CharField(help_text='Geben Sie die Antwort2 der Frage ein', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='frage',
            name='antwort2richtig',
            field=models.BooleanField(default=False, help_text='Geben Sie an ob Antwort2 richtig ist'),
        ),
        migrations.AddField(
            model_name='frage',
            name='antwort3',
            field=models.CharField(blank=True, help_text='Geben Sie die Antwort3 der Frage ein (optional)', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='frage',
            name='antwort3richtig',
            field=models.BooleanField(default=False, help_text='Geben Sie an ob Antwort3 richtig ist'),
        ),
        migrations.AddField(
            model_name='frage',
            name='antwort4',
            field=models.CharField(blank=True, help_text='Geben Sie die Antwort4 der Frage ein (optional)', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='frage',
            name='antwort4richtig',
            field=models.BooleanField(default=False, help_text='Geben Sie an ob Antwort4 richtig ist'),
        ),
    ]
