# Generated by Django 3.1.7 on 2021-03-09 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='Country Code')),
                ('name', models.CharField(max_length=32, verbose_name='Country Name')),
                ('parent_code', models.IntegerField(verbose_name='Country Parent Code')),
                ('iso_code', models.CharField(max_length=5, verbose_name='Country ISO Code')),
                ('type', models.CharField(max_length=32, verbose_name='Country Type')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='Location Code')),
                ('name', models.CharField(max_length=32, verbose_name='Location Name')),
                ('parent_code', models.IntegerField(verbose_name='Location Parent Code')),
                ('type', models.CharField(max_length=32, verbose_name='Location Type')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.country')),
            ],
        ),
    ]
