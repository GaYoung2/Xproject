# Generated by Django 3.0.7 on 2020-06-18 13:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('row', models.IntegerField(null=True)),
                ('column', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('seat_id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False)),
                ('missed_time', models.FloatField(null=True)),
                ('status', models.CharField(blank=True, choices=[('u', 'Use'), ('m', 'Missed'), ('a', 'Available')], default='a', help_text='Present Sit Status', max_length=1)),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='smartstudyroom.Room')),
            ],
        ),
    ]