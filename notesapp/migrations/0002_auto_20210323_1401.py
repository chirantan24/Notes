# Generated by Django 3.1.5 on 2021-03-23 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='notesapp.user'),
        ),
    ]
