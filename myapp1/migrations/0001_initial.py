# Generated by Django 3.2.6 on 2021-09-14 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=10)),
                ('course_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idn', models.CharField(max_length=10)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=10)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_id', models.CharField(max_length=10)),
                ('subject_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_id', models.IntegerField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.course')),
                ('idn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.student')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.subject')),
            ],
        ),
    ]
