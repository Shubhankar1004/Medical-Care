# Generated by Django 4.0.4 on 2022-04-26 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='feedback_email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='feedback',
            new_name='Message',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='feedback_by',
            new_name='Name',
        ),
    ]
