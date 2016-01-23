# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.management import call_command
from django.db import migrations, models

initial_categories_data = [
    {
        'name': 'Security | Health | Body',
        'order': 1,
    },
    {
        'name': 'Pleasure | Entertainment | Fun',
        'order': 2,
    },
    {
        'name': 'Confidence | Career | Money',
        'order': 3,
    },
    {
        'name': 'Compassion | Environment | Home',
        'order': 4,
    },
    {
        'name': 'Communication | Social | People',
        'order': 5,
    },
    {
        'name': 'Vision | Mental | Mind',
        'order': 6,
    },
    {
        'name': 'Purpose | Spiritual | Soul',
        'order': 7,
    },
]


def create_initial_categories(apps, schema_editor):
    Category = apps.get_model('categories', 'Category')
    db_alias = schema_editor.connection.alias
    categories = []
    for data in initial_categories_data:
        category = Category(
            name=data.get('name'),
            order=data.get('order'),
        )
        categories.append(category)
    Category.objects.using(db_alias).bulk_create(categories)


def delete_initial_categories(apps, schema_editor):
    Category = apps.get_model('categories', 'Category')
    db_alias = schema_editor.connection.alias
    Category.objects.using(db_alias).filter(order__gte=0, order__lte=7).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('categories', '0003_auto_20160108_2040'),
    ]

    operations = [
        migrations.RunPython(create_initial_categories, delete_initial_categories),
    ]
