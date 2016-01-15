# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import textwrap

from django.db import migrations

initial_cards_data = [
    {
        'name': 'Outer Call',
        'sort_order': 1,
        'content': "Reflect on how and why you got to coLegend by answering the questions to the Outer Call.",
        'details': "- click: “connected” → “Legend” →  “Outer Call”",
        'category': 6,
    },
    {
        'name': 'Inner Call',
        'sort_order': 2,
        'content': "Become conscious about your motivation to coLegend and fill out your Inner Call.",
        'details': "-click: “connected” → “Legend” →  “Inner Call”",
        'category': 6,
    },
    {
        'name': 'Biography',
        'sort_order': 3,
        'content': "Take some time to acknowledge and celebrate the challenges and accomplishments in your life so far. Write your biography.",
        'details': "-click: “connected” → “Legend” →  “Biography”",
        'category': 6,
    },
    {
        'name': 'About',
        'sort_order': 4,
        'content': "Share some basic facts about yourself with your fellow legends and fill out the “About” part of your legend profile.",
        'details': textwrap.dedent("""\
            - click: “connected” → “Legend”
            - Find the “About” section.
            - There is now a little edit icon. Click on it."""),
        'category': 5,
    },
    {
        'name': 'Guidelines',
        'sort_order': 5,
        'content': "Become a legitimate member of the coLegend community by reading and accepting the community guidelines.",
        'details': "-click: “connected” → “Guidelines”",
        'category': 5,
    },
    {
        'name': 'Chat',
        'sort_order': 6,
        'content': "Connect yourself with other fellow legends by registering for our chat programm Slack.",
        'details': "-click: “connected” → “Chat”",
        'category': 5,
    },
    {
        'name': 'Cloud Guide',
        'sort_order': 7,
        'content': "Check out your Cloud Guide Page and see whether you’ve already been found by your Cloud Guide.",
        'details': "-click: “connected” → “Cloud Guide”",
        'category': 5,
    },
    {
        'name': 'Storytime',
        'sort_order': 8,
        'content': "You’ve done quite a bit. Now it’s time for relaxing and enjoying your first story of coLegend’s fantastical world Leyenda.",
        'details': "-click: “continuous” → “Story” → ?",
        'category': 2,
    },
]


def create_initial_cards(apps, schema_editor):
    Card = apps.get_model('cards', 'Card')
    Category = apps.get_model('categories', 'Category')
    db_alias = schema_editor.connection.alias
    cards = []
    for data in initial_cards_data:
        card = Card.objects.create(
            name=data.get('name'),
            sort_order=data.get('sort_order'),
            content=data.get('content'),
            details=data.get('details'),
        )
        cards.append(card)
        # add category
        category_order = data.get('category')
        category = Category.objects.get(order=category_order)
        card.category.add(category)
        # Card.objects.using(db_alias).bulk_create(cards)


def delete_initial_cards(apps, schema_editor):
    Card = apps.get_model('cards', 'Card')
    db_alias = schema_editor.connection.alias
    Card.objects.using(db_alias).filter(sort_order__gte=0, sort_order__lte=8).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('cards', '0002_auto_20160114_0455'),
        ('categories', '0004_load_initial_data'),
    ]

    operations = [
        migrations.RunPython(create_initial_cards, delete_initial_cards),
    ]
