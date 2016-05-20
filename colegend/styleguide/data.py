# -*- coding: utf-8 -*-
# Data for the styleguide context
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.templatetags.static import static

from colegend.core.utils.icons import icon_dict
from .models import Element, ElementGroup

Legend = get_user_model()

atoms = []

logo = Element(
    'Default',
    template='atoms/logo.html',
    context={
        'url': static('images/coLegendLogo_86x18.png'),
    }
)
logo_colored = Element(
    'Default',
    template='atoms/logo.html',
    context={
        'url': static('images/coLegendLogo_white_86x18.png'),
        'class': 'bg-main-dark',
    }
)
favicon = Element(
    'favicon',
    template='atoms/logo.html',
    context={
        'url': static('images/favicon.ico'),
    }
)

logos = ElementGroup('Logos', columns=4, elements=[logo, logo_colored, favicon])

atoms.append(logos)

color_main = Element(
    'Main',
    template='styleguide/atoms/color.html',
    context={
        'name': 'main',
    }
)
color_main_light = Element(
    'Main light',
    template='styleguide/atoms/color.html',
    context={
        'name': 'main-light',
    }
)
color_main_dark = Element(
    'Main dark',
    template='styleguide/atoms/color.html',
    context={
        'name': 'main-dark',
    }
)
color_accent = Element(
    'Accent',
    template='styleguide/atoms/color.html',
    context={
        'name': 'accent',
    }
)
color_accent_light = Element(
    'Accent light',
    template='styleguide/atoms/color.html',
    context={
        'name': 'accent-light',
    }
)
color_accent_dark = Element(
    'Accent dark',
    template='styleguide/atoms/color.html',
    context={
        'name': 'accent-dark',
    }
)

project_colors = ElementGroup(
    'Project colors',
    columns=4,
    elements=[
        color_main, color_main_light, color_main_dark,
        color_accent, color_accent_light, color_accent_dark
    ]
)

color_category_1 = Element(
    'Catagrory 1',
    template='styleguide/atoms/color.html',
    context={
        'name': 'category-1',
    }
)
color_category_2 = Element(
    'Catagrory 2',
    template='styleguide/atoms/color.html',
    context={
        'name': 'category-2',
    }
)
color_category_3 = Element(
    'Catagrory 3',
    template='styleguide/atoms/color.html',
    context={
        'name': 'category-3',
    }
)
color_category_4 = Element(
    'Catagrory 4',
    template='styleguide/atoms/color.html',
    context={
        'name': 'category-4',
    }
)
color_category_5 = Element(
    'Catagrory 5',
    template='styleguide/atoms/color.html',
    context={
        'name': 'category-5',
    }
)
color_category_6 = Element(
    'Catagrory 6',
    template='styleguide/atoms/color.html',
    context={
        'name': 'category-6',
    }
)
color_category_7 = Element(
    'Catagrory 7',
    template='styleguide/atoms/color.html',
    context={
        'name': 'category-7',
    }
)

category_colors = ElementGroup(
    'Catagory colors',
    columns=4,
    elements=[
        color_category_1, color_category_2, color_category_3,
        color_category_4, color_category_5, color_category_6,
        color_category_7
    ]
)

color_primary = Element(
    'Primary',
    template='styleguide/atoms/color.html',
    context={
        'name': 'primary',
    }
)
color_success = Element(
    'Success',
    template='styleguide/atoms/color.html',
    context={
        'name': 'success',
    }
)
color_info = Element(
    'Info',
    template='styleguide/atoms/color.html',
    context={
        'name': 'info',
    }
)
color_warning = Element(
    'Warning',
    template='styleguide/atoms/color.html',
    context={
        'name': 'warning',
    }
)
color_danger = Element(
    'Danger',
    template='styleguide/atoms/color.html',
    context={
        'name': 'danger',
    }
)

action_colors = ElementGroup(
    'Action colors',
    columns=4,
    elements=[
        color_primary, color_success, color_info, color_warning, color_danger,
    ]
)

colors = ElementGroup(
    'Colors',
    columns=12,
    elements=[
        project_colors, category_colors, action_colors,
    ]
)

atoms.append(colors)

headline_1 = Element(
    'Headline 1',
    template='atoms/headline.html',
    context={
        'text': 'Heading Level 1',
    }
)
headline_2 = Element(
    'Headline 2',
    template='atoms/headline.html',
    context={
        'text': 'Heading Level 2',
        'level': 2,
    }
)
headline_3 = Element(
    'Headline 3',
    template='atoms/headline.html',
    context={
        'text': 'Heading Level 3',
        'level': 3,
    }
)
headline_4 = Element(
    'Headline 4',
    template='atoms/headline.html',
    context={
        'text': 'Heading Level 4',
        'level': 4,
    }
)
headline_5 = Element(
    'Headline 5',
    template='atoms/headline.html',
    context={
        'text': 'Heading Level 5',
        'level': 5,
    }
)
headline_6 = Element(
    'Headline 6',
    template='atoms/headline.html',
    context={
        'text': 'Heading Level 6',
        'level': 6,
    }
)

headlines = ElementGroup(
    'Headlines',
    columns=12,
    elements=[
        headline_1, headline_2, headline_3, headline_4, headline_5, headline_6,
    ]
)

atoms.append(headlines)

link = Element(
    'Link',
    template='styleguide/atoms/link.html',
    context={
    }
)

atoms.append(link)

icons = Element(
    'Icons',
    template='styleguide/molecules/icons.html',
    context={
        'icons': [{'name': icon} for icon in icon_dict]
    }
)

atoms.append(icons)

link_button = Element(
    'Link button',
    template='atoms/button.html',
    context={
        'text': 'Link',
        'class': 'btn-link',
    }
)
action_button = Element(
    'Action button',
    template='atoms/button.html',
    context={
        'text': 'Action',
        'class': 'btn-primary',
    }
)
secondary_button = Element(
    'Secondary button',
    template='atoms/button.html',
    context={
        'text': 'Secondary',
        'class': 'btn-secondary',
    }
)
icon_button = Element(
    'Button with icon',
    template='atoms/button.html',
    context={
        'text': 'Star',
        'icon': 'star',
        'class': 'btn-primary',
    }
)
linked_button = Element(
    'Button with link',
    template='atoms/button.html',
    context={
        'text': 'Click Me',
        'class': 'btn-primary',
        'url': 'https://www.google.com',
    }
)
success_button = Element(
    'Success button',
    template='atoms/button.html',
    context={
        'text': 'Yeah!',
        'class': 'btn-success',
    }
)
info_button = Element(
    'Info button',
    template='atoms/button.html',
    context={
        'text': 'More info',
        'class': 'btn-info',
    }
)
warning_button = Element(
    'Warning button',
    template='atoms/button.html',
    context={
        'text': 'Caution',
        'class': 'btn-warning',
    }
)
danger_button = Element(
    'Danger button',
    template='atoms/button.html',
    context={
        'text': 'Delete',
        'class': 'btn-danger',
    }
)
small_button = Element(
    'Small button',
    template='atoms/button.html',
    context={
        'text': 'Mini',
        'class': 'btn-primary btn-sm',
    }
)
large_button = Element(
    'Large button',
    template='atoms/button.html',
    context={
        'text': 'Special Offer',
        'class': 'btn-primary btn-lg',
    }
)
outline_button = Element(
    'Outline button',
    template='atoms/button.html',
    context={
        'text': 'Optional',
        'class': 'btn-info-outline',
    }
)
disabled_button = Element(
    'Disabled button',
    template='atoms/button.html',
    context={
        'text': 'Locked',
        'class': 'btn-primary disabled',
    }
)

primary_feedback_button = Element(
    'Primary feedback button',
    template='atoms/image.html',
    context={
        'url': static('images/feedback.png'),
        'class': 'img-responsive',
        'name': 'feedback button',
    },
)

accented_feedback_button = Element(
    'Accented feedback button',
    template='atoms/image.html',
    context={
        'url': static('images/feedback_accented_dark.png'),
        'class': 'img-responsive',
        'name': 'feedback button accented',
    },
)

buttons = ElementGroup(
    'Buttons',
    columns=3,
    elements=[
        link_button, action_button, secondary_button,
        icon_button, linked_button,
        success_button, info_button, warning_button, danger_button,
        small_button, large_button,
        outline_button, disabled_button,
        primary_feedback_button, accented_feedback_button,
    ]
)

atoms.append(buttons)

label = Element(
    'Simple label',
    template='atoms/label.html',
    context={
        'text': 'Information',
    }
)
accented_label = Element(
    'Accented label',
    template='atoms/label.html',
    context={
        'text': 'Information',
        'class': 'bg-accent',
    }
)
rounded_warning_label = Element(
    'Rounded warning label',
    template='atoms/label.html',
    context={
        'text': 'Warning!',
        'class': 'label-pill bg-warning',
    }
)

labels = ElementGroup(
    'Labels',
    columns=3,
    elements=[
        label, accented_label, rounded_warning_label,
    ]
)

atoms.append(labels)

speech_bubble_right = Element(
    'Simple bubble',
    template='atoms/speech-bubble.html',
    context={
        'content': 'arrow left',
    }
)
speech_bubble_left = Element(
    'Bubble left',
    template='atoms/speech-bubble.html',
    context={
        'content': 'arrow right',
        'arrow': 'right',
    }
)
speech_bubble_top = Element(
    'Bubble top',
    template='atoms/speech-bubble.html',
    context={
        'content': 'arrow down',
        'arrow': 'down',
    }
)
speech_bubble_bottom = Element(
    'Bubble bottom',
    template='atoms/speech-bubble.html',
    context={
        'content': 'arrow up',
        'arrow': 'up',
    }
)

speeach_bubbles = ElementGroup(
    'Speech bubbles',
    columns=3,
    elements=[
        speech_bubble_right, speech_bubble_left, speech_bubble_top, speech_bubble_bottom,
    ]
)

atoms.append(speeach_bubbles)

anonymous_avatar = Element(
    'Anonymous avatar',
    template='atoms/avatar.html',
    context={
        'name': 'Anonymous',
        'image': 'legends/images/anonymous.png',
        'label': {
            'class': 'label-pill bg-accent',
        },
    }
)
legend_avatar = Element(
    'Legend avatar',
    template='atoms/avatar.html',
    context={
        'image': 'legends/images/npc/Coralina.png',
        'name': 'Coralina Charming',
        'url': '#coralina',
        'label': {
            'class': 'label-pill bg-accent',
        },
    }
)
small_avatar = Element(
    'Small avatar',
    template='atoms/avatar.html',
    context={
        'image': 'legends/images/npc/Coralina.png',
        'name': 'Coralina Charming',
        'url': '#coralina',
        'size': 'small',
        'label': {
            'class': 'label-pill bg-accent',
        },
    }
)
large_avatar = Element(
    'Large avatar',
    template='atoms/avatar.html',
    context={
        'image': 'legends/images/npc/Coralina.png',
        'name': 'Coralina Charming',
        'url': '#coralina',
        'size': 'large',
        'label': {
            'class': 'label-pill bg-accent',
        },
    }
)

avatars = ElementGroup(
    'Avatars',
    columns=3,
    elements=[
        anonymous_avatar, legend_avatar, small_avatar, large_avatar
    ]
)

atoms.append(avatars)

cake_badge = Element(
    'Cake badge',
    template='atoms/badge.html',
    context={
        'name': 'Cake',
        'image': 'styleguide/images/icon_cake.png',
        'class': 'bg-category-3',
        'label': {
            'class': 'bg-accent',
        },
    }
)
camera_badge = Element(
    'Camera badge',
    template='atoms/badge.html',
    context={
        'name': 'Camera',
        'image': 'styleguide/images/icon_camera.png',
        'class': 'bg-category-5',
        'label': {
            'class': 'bg-accent',
        },
    }
)

badges = ElementGroup(
    'Badges',
    columns=3,
    elements=[
        cake_badge, camera_badge,
    ]
)

atoms.append(badges)

molecules = []

horizontal_button_group = Element(
    'Horizontal buttons',
    template='molecules/buttons.html',
    context={
        'buttons': [
            {
                'text': 'Button 1',
                'class': 'btn-primary',
            },
            {
                'text': 'Button 2',
                'class': 'btn-primary',
            },
            {
                'text': 'Button 3',
                'class': 'btn-primary',
            },
        ],
    }
)
small_button_group = Element(
    'Small buttons',
    template='molecules/buttons.html',
    context={
        'buttons': [
            {
                'text': 'Button 1',
                'class': 'btn-primary',
            },
            {
                'text': 'Button 2',
                'class': 'btn-primary',
            },
            {
                'text': 'Button 3',
                'class': 'btn-primary',
            },
        ],
        'class': 'btn-group btn-group-sm',
    }
)
small_vertical_button_group = Element(
    'Small vertical buttons',
    template='molecules/buttons.html',
    context={
        'buttons': [
            {
                'text': 'Button 1',
                'class': 'btn-primary',
            },
            {
                'text': 'Button 2',
                'class': 'btn-primary',
            },
            {
                'text': 'Button 3',
                'class': 'btn-primary',
            },
        ],
        'class': 'btn-group-vertical',
    }
)

button_groups = ElementGroup(
    'Button groups',
    columns=12,
    elements=[
        horizontal_button_group, small_button_group, small_vertical_button_group,
    ]
)

molecules.append(button_groups)

left_avatar_statement = Element(
    'Left statement',
    template='molecules/avatar-statement.html',
    context={
        'name': 'Coralina Charming',
        'url': '#coralina',
        'label': {'class': 'label-pill bg-accent'},
        'image': 'legends/images/npc/Coralina.png',
        # statement
        'content': 'Hello world!',
        'arrow': 'left pull-up',
        'responsive_arrow': 'up',
    },
    columns=8,
)

right_avatar_statement = Element(
    'Right statement',
    template='molecules/avatar-statement.html',
    context={
        'name': 'Coralina Charming',
        'url': '#coralina',
        'label': {'class': 'label-pill bg-accent'},
        'image': 'legends/images/npc/Coralina.png',
        # statement
        'content': 'This is my answer',
        'arrow': 'right pull-up',
        'responsive_arrow': 'up',
        'avatar_class': 'col-sm-4 col-sm-push-8',
        'bubble_class': 'col-sm-8  col-sm-pull-4',
    },
    columns=8,
)

big_avatar_statement = Element(
    'Big statement',
    template='molecules/avatar-statement.html',
    context={
        'name': 'Coralina Charming',
        'url': '#coralina',
        'label': {'class': 'label-pill bg-accent'},
        'image': 'legends/images/npc/Coralina.png',
        'size': 'large',
        # statement
        'content': 'This is my answer',
        'arrow': 'left pull-up',
        'responsive_arrow': 'up',
        'avatar_class': 'col-sm-4',
        'bubble_class': 'col-sm-8',
    },
)

small_avatar_statement = Element(
    'Small statement',
    template='molecules/avatar-statement.html',
    context={
        'name': 'Coralina Charming',
        'url': '#coralina',
        'label': {'class': 'label-pill bg-accent'},
        'image': 'legends/images/npc/Coralina.png',
        'size': 'small',
        # statement
        'content': 'This is my answer',
        'arrow': 'left pull-up',
        'responsive_arrow': 'up',
        'avatar_class': 'col-sm-4',
        'bubble_class': 'col-sm-8',
    },
    columns=6
)

avatar_statements = ElementGroup(
    'Avatar statements',
    elements=[
        left_avatar_statement, right_avatar_statement, big_avatar_statement, small_avatar_statement,
    ]
)

molecules.append(avatar_statements)

organisms = []

simple_card = Element(
    'Simple card',
    template='organisms/card.html',
    context={
        'content': 'Hello World',
    }
)
card_with_title = Element(
    'Card with title',
    template='organisms/card.html',
    context={
        'title': {
            'content': 'Hello',
        },
        'content': 'Hello World',
    }
)
card_with_header = Element(
    'Card with header',
    template='organisms/card.html',
    context={
        'header': {
            'content': 'Hello above',
        },
        'content': 'Hello World',
    }
)
card_with_footer = Element(
    'Card with footer',
    template='organisms/card.html',
    context={
        'footer': {
            'content': 'Hello below',
        },
        'content': 'Hello World',
    }
)
dismissable_card = Element(
    'Dismissable card',
    template='organisms/card.html',
    context={
        'closeable': True,
        'content': 'Close me!',
    }
)
full_card = Element(
    'Full card',
    template='organisms/card.html',
    context={
        'closeable': True,
        'header': {
            'content': 'Hello above',
        },
        'content': 'Close me!',
        'footer': {
            'content': 'Hello below',
        },
    }
)

cards = ElementGroup(
    'Cards',
    columns=6,
    elements=[
        simple_card, card_with_title, card_with_header, card_with_footer, dismissable_card, full_card,
    ]
)

organisms.append(cards)

anonymous_navigation_bar = Element(
    'Anonymous navigation bar',
    template='organisms/navbar.html',
    context={
        'id': 'anonymous-bar',
        'menu_id': 'styleguide',
        'class': 'bg-main-dark',
        'user': AnonymousUser(),
    }
)
legend_navigation_bar = Element(
    'Legend navigation bar',
    template='organisms/navbar.html',
    context={
        'id': 'legend-bar',
        'menu_id': 'styleguide',
        'class': 'bg-main-dark',
        'user': Legend.objects.get_or_create(username='Demo')[0],
    }
)

navigations = ElementGroup(
    'Navigations',
    columns=12,
    elements=[
        anonymous_navigation_bar, legend_navigation_bar,
    ]
)

organisms.append(navigations)

simple_header = Element(
    'Simple header',
    template='organisms/header.html',
    context={
        'title': 'Page Title Test',
    }
)

full_header = Element(
    'Header with breadcrumbs links and controls',
    template='organisms/header.html',
    context={
        'title': 'Page Title Test',
        'breadcrumbs': [
            {
                'name': 'Link 1',
                'url': '#link1',
            },
            {
                'name': 'Link 2',
                'url': '#link2',
            },
            {
                'name': 'Link 3',
                'url': '#link3',
            },
        ],
        'links': [
            {
                'text': 'Link 1',
                'class': 'btn-link',
            },
            {
                'text': 'Link 2',
                'class': 'btn-link',
            },
            {
                'text': 'Link 3',
                'class': 'btn-link',
            },
        ],
        'buttons': [
            {
                'text': 'Button 1',
                'class': 'btn-primary',
            },
            {
                'text': 'Button 2',
                'class': 'btn-primary',
            },
            {
                'text': 'Button 3',
                'class': 'btn-primary',
            },
        ],
    }
)

headers = ElementGroup(
    'Headers',
    columns=12,
    elements=[
        simple_header, full_header,
    ]
)

organisms.append(headers)
