# Generated by Django 4.1.2 on 2023-03-22 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='subjectInCharge',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='main.courses'),
        ),
    ]
