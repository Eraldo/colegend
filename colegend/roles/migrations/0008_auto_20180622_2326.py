# Generated by Django 2.0.4 on 2018-06-22 21:26

import colegend.core.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0007_role_metrics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('purpose', colegend.core.fields.MarkdownField(verbose_name='purpose')),
                ('strategy', colegend.core.fields.MarkdownField(blank=True, verbose_name='strategy')),
                ('domains', colegend.core.fields.MarkdownField(blank=True, verbose_name='domains')),
                ('accountabilities', colegend.core.fields.MarkdownField(blank=True, verbose_name='accountabilities')),
                ('policies', colegend.core.fields.MarkdownField(blank=True, verbose_name='policies')),
                ('history', colegend.core.fields.MarkdownField(blank=True, verbose_name='history')),
                ('notes', colegend.core.fields.MarkdownField(blank=True, verbose_name='history')),
                ('checklists', colegend.core.fields.MarkdownField(blank=True, verbose_name='checklists')),
                ('metrics', colegend.core.fields.MarkdownField(blank=True, verbose_name='metrics')),
            ],
            options={
                'default_related_name': 'circles',
            },
        ),
        migrations.AddField(
            model_name='role',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='role',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
