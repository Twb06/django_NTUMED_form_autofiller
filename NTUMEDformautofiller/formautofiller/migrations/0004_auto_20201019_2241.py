# Generated by Django 3.1.2 on 2020-10-19 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formautofiller', '0003_auto_20201019_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='student',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='formautofiller.student'),
        ),
    ]
