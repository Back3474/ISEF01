# Generated by Django 3.2 on 2022-02-10 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20211209_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frage',
            name='name',
            field=models.CharField(help_text='Geben Sie die Frage ein', max_length=255),
        ),
        migrations.CreateModel(
            name='RichtigOderFalsch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Geben Sie die Frage ein', max_length=255)),
                ('behauptungrichtig', models.BooleanField(default=False, help_text='Ist diese Frage wahr?')),
                ('kurs', models.ForeignKey(help_text='Wählen Sie den Kurs, welchem die Frage zugewiesen wird', null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.kurs')),
            ],
        ),
    ]
