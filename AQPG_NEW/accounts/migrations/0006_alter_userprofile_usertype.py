# Generated by Django 4.1.2 on 2023-03-22 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_userprofile_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='userType',
            field=models.CharField(choices=[('0', 'Teacher'), ('1', 'Expert')], default='0', max_length=20),
        ),
    ]
