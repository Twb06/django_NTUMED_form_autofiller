# Generated by Django 3.1.2 on 2020-10-19 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(choices=[('2', 'A: Perfect'), ('3', 'B: Good'), ('4', 'C: Normal'), ('5', 'D: Bad'), ('6', 'E: Lame')], default='2', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(help_text='Enter your name', max_length=10)),
                ('student_id', models.UUIDField(help_text='Enter your student id', primary_key=True, serialize=False)),
                ('teacher', models.CharField(help_text='Enter your teacher name', max_length=5)),
                ('email', models.EmailField(help_text='Enter your email', max_length=254)),
                ('preference', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='formautofiller.preference')),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter form name', max_length=10)),
                ('form_url', models.URLField(help_text='Enter form url')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='formautofiller.student')),
            ],
        ),
    ]
