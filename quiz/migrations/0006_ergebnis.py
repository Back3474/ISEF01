# Generated by Django 3.2 on 2022-02-10 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20220210_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ergebnis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testmodus', models.CharField(max_length=20)),
                ('benutzername', models.CharField(max_length=50)),
                ('kursid', models.CharField(max_length=5)),
                ('kursname', models.CharField(max_length=50)),
                ('zeitsekunden', models.IntegerField()),
                ('datum', models.DateField(auto_now_add=True)),
                ('punkte', models.IntegerField()),
                ('fragentotal', models.IntegerField()),
                ('fragenkorrekt', models.IntegerField()),
                ('fragenfalsch', models.IntegerField()),
            ],
        ),
    ]
