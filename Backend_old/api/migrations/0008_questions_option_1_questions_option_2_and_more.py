# Generated by Django 4.1.3 on 2022-11-13 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_mcq'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='option_1',
            field=models.CharField(blank=True, default='default', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='option_2',
            field=models.CharField(blank=True, default='default', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='option_3',
            field=models.CharField(blank=True, default='default', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='option_4',
            field=models.CharField(blank=True, default='default', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='type',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
