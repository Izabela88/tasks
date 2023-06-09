# Generated by Django 3.0.9 on 2023-03-23 14:14

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('LIVE', 'LIVE'), ('PENDING', 'PENDING'), ('ARCHIVED', 'ARCHIVED')], max_length=50)),
                ('launch_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('order', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('task_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='task.TaskType')),
                ('tile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='task.Tile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
