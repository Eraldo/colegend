# Generated by Django 2.0.4 on 2018-07-13 12:29

import colegend.core.fields
import colegend.core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journey', '0024_hero_topics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('content', colegend.core.fields.MarkdownField(blank=True, verbose_name='content')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tensions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_related_name': 'tensions',
            },
            bases=(colegend.core.models.OwnedCheckMixin, models.Model),
        ),
        migrations.AlterField(
            model_name='demon',
            name='content',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='demon',
            name='fears',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='fears'),
        ),
        migrations.AlterField(
            model_name='demon',
            name='name',
            field=models.CharField(default='Demon', max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='demon',
            name='tensions',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='tensions'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='achievements',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='achievements'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='blueprint_day',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='day blueprint'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='blueprint_month',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='month blueprint'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='blueprint_week',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='week blueprint'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='bucket',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='bucket list'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='content',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='experiments',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='experiments'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='goals',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='goals'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='habits',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='habits'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='inspirations',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='inspirations'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='mission',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='mission'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='name',
            field=models.CharField(default='Hero', max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='people',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='people'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='powers',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='powers'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='principles',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='principles'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='projects',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='projects'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='questions',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='questions'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='resources',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='resources'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='roles',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='roles'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='routines',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='routines'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='skills',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='skills'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='strategy',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='strategy'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='topics',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='topics'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='values',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='values'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='vision',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='vision'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='wishes',
            field=colegend.core.fields.MarkdownField(blank=True, verbose_name='wishes'),
        ),
    ]
