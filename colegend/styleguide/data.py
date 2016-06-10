# -*- coding: utf-8 -*-
# Data for the styleguide context
from django.contrib.auth.models import AnonymousUser
from django.templatetags.static import static
from django.utils import timezone
from django.utils.html import format_html

from colegend.core.templatetags.core_tags import image, icon
from colegend.core.utils.icons import icons
from .models import Widget, WidgetGroup, TagWidget

widgets = []

widgets.append(
    TagWidget(
        'Styleguide widget example',
        tag='headline',
        libraries='core_tags',
        parameters={
            'content': 'Headline widget example as tag with comments',
            'level': 4,
        },
        comment='Help foo\nbla',
    )
)

logo = Widget(
    'Default',
    template='widgets/div.html',
    context={
        'content': image(static('images/coLegendLogo_86x18.png'), name='logo'),
        'classes': 'card-block',
    }
)
logo_colored = Widget(
    'Default',
    template='widgets/div.html',
    context={
        'content': image(static('images/coLegendLogo_white_86x18.png'), name='logo inverted'),
        'classes': 'card-block bg-main-dark',
    }
)
favicon = Widget(
    'favicon',
    template='widgets/div.html',
    context={
        'content': image(static('images/favicon.ico'), name='favicon'),
        'classes': 'card-block',
    }
)

logos = WidgetGroup('Logos', columns=4, widgets=[logo, logo_colored, favicon])

widgets.append(logos)

color_main = Widget(
    'Main',
    template='styleguide/widgets/color.html',
    context={
        'name': 'main',
    }
)
color_main_light = Widget(
    'Main light',
    template='styleguide/widgets/color.html',
    context={
        'name': 'main-light',
    }
)
color_main_dark = Widget(
    'Main dark',
    template='styleguide/widgets/color.html',
    context={
        'name': 'main-dark',
    }
)
color_accent = Widget(
    'Accent',
    template='styleguide/widgets/color.html',
    context={
        'name': 'accent',
    }
)
color_accent_light = Widget(
    'Accent light',
    template='styleguide/widgets/color.html',
    context={
        'name': 'accent-light',
    }
)
color_accent_dark = Widget(
    'Accent dark',
    template='styleguide/widgets/color.html',
    context={
        'name': 'accent-dark',
    }
)

project_colors = WidgetGroup(
    'Project colors',
    columns=4,
    widgets=[
        color_main, color_main_light, color_main_dark,
        color_accent, color_accent_light, color_accent_dark
    ]
)

color_category_1 = Widget(
    'Catagrory 1',
    template='styleguide/widgets/color.html',
    context={
        'name': 'category-1',
    }
)
color_category_2 = Widget(
    'Catagrory 2',
    template='styleguide/widgets/color.html',
    context={
        'name': 'category-2',
    }
)
color_category_3 = Widget(
    'Catagrory 3',
    template='styleguide/widgets/color.html',
    context={
        'name': 'category-3',
    }
)
color_category_4 = Widget(
    'Catagrory 4',
    template='styleguide/widgets/color.html',
    context={
        'name': 'category-4',
    }
)
color_category_5 = Widget(
    'Catagrory 5',
    template='styleguide/widgets/color.html',
    context={
        'name': 'category-5',
    }
)
color_category_6 = Widget(
    'Catagrory 6',
    template='styleguide/widgets/color.html',
    context={
        'name': 'category-6',
    }
)
color_category_7 = Widget(
    'Catagrory 7',
    template='styleguide/widgets/color.html',
    context={
        'name': 'category-7',
    }
)

category_colors = WidgetGroup(
    'Catagory colors',
    columns=4,
    widgets=[
        color_category_1, color_category_2, color_category_3,
        color_category_4, color_category_5, color_category_6,
        color_category_7
    ]
)

color_primary = Widget(
    'Primary',
    template='styleguide/widgets/color.html',
    context={
        'name': 'primary',
    }
)
color_success = Widget(
    'Success',
    template='styleguide/widgets/color.html',
    context={
        'name': 'success',
    }
)
color_info = Widget(
    'Info',
    template='styleguide/widgets/color.html',
    context={
        'name': 'info',
    }
)
color_warning = Widget(
    'Warning',
    template='styleguide/widgets/color.html',
    context={
        'name': 'warning',
    }
)
color_danger = Widget(
    'Danger',
    template='styleguide/widgets/color.html',
    context={
        'name': 'danger',
    }
)

action_colors = WidgetGroup(
    'Action colors',
    columns=4,
    widgets=[
        color_primary, color_success, color_info, color_warning, color_danger,
    ]
)

colors = WidgetGroup(
    'Colors',
    columns=12,
    widgets=[
        project_colors, category_colors, action_colors,
    ]
)

widgets.append(colors)

headline_1 = Widget(
    'Headline 1',
    template='widgets/headline.html',
    context={
        'content': 'Heading Level 1',
        'level': 1,
    }
)
headline_2 = Widget(
    'Headline 2',
    template='widgets/headline.html',
    context={
        'content': 'Heading Level 2',
        'level': 2,
    }
)
headline_3 = Widget(
    'Headline 3',
    template='widgets/headline.html',
    context={
        'content': 'Heading Level 3',
        'level': 3,
    }
)
headline_4 = Widget(
    'Headline 4',
    template='widgets/headline.html',
    context={
        'content': 'Heading Level 4',
        'level': 4,
    }
)
headline_5 = Widget(
    'Headline 5',
    template='widgets/headline.html',
    context={
        'content': 'Heading Level 5',
        'level': 5,
    }
)
headline_6 = Widget(
    'Headline 6',
    template='widgets/headline.html',
    context={
        'content': 'Heading Level 6',
        'level': 6,
    }
)

headlines = WidgetGroup(
    'Headlines',
    columns=12,
    widgets=[
        headline_1, headline_2, headline_3, headline_4, headline_5, headline_6,
    ]
)

widgets.append(headlines)

link_simple = Widget(
    'Simple link',
    template='widgets/link.html',
    context={
        'content': 'foo bar',
        'url': '#foobar',
    }
)

link_external = Widget(
    'External link',
    template='widgets/link.html',
    context={
        'content': 'google',
        'url': 'http://www.google.com',
        'external': True,
    }
)

link_legend = Widget(
    'Legend link',
    template='widgets/link.html',
    context={
        'content': 'Coralina',
        'url': '#coralina',
    }
)

links = WidgetGroup(
    'Links',
    columns=4,
    widgets=[
        link_simple, link_external, link_legend,
    ]
)

widgets.append(links)

WidgetGroup(
    'Links',
    columns=4,
    widgets=[
        link_simple, link_external, link_legend,
    ]
)

widgets.append(
    WidgetGroup(
        'Icons',
        columns=3,
        widgets=[
            Widget(
                '{} icon'.format(name),
                template='widgets/icon.html',
                context={'classes': icon(name, raw=True)}) for name in icons
            ]
    )
)

link_button = Widget(
    'Link button',
    template='widgets/button.html',
    context={
        'content': 'Link',
        'classes': 'btn btn-link',
    }
)
action_button = Widget(
    'Action button',
    template='widgets/button.html',
    context={
        'content': 'Action',
        'classes': 'btn btn-primary',
    }
)
secondary_button = Widget(
    'Secondary button',
    template='widgets/button.html',
    context={
        'content': 'Secondary',
        'classes': 'btn btn-secondary',
    }
)
icon_button = Widget(
    'Button with icon',
    template='widgets/button.html',
    context={
        'content': format_html('{} {}', Widget.get('Challenges icon'), 'Star'),
        'classes': 'btn btn-primary',
    }
)
linked_button = Widget(
    'Button with link',
    template='widgets/button.html',
    context={
        'content': 'Click Me',
        'classes': 'btn btn-primary',
        'url': 'https://www.google.com',
    }
)
success_button = Widget(
    'Success button',
    template='widgets/button.html',
    context={
        'content': 'Yeah!',
        'classes': 'btn btn-success',
    }
)
info_button = Widget(
    'Info button',
    template='widgets/button.html',
    context={
        'content': 'More info',
        'classes': 'btn btn-info',
    }
)
warning_button = Widget(
    'Warning button',
    template='widgets/button.html',
    context={
        'content': 'Caution',
        'classes': 'btn btn-warning',
    }
)
danger_button = Widget(
    'Danger button',
    template='widgets/button.html',
    context={
        'content': 'Delete',
        'classes': 'btn btn-danger',
    }
)
small_button = Widget(
    'Small button',
    template='widgets/button.html',
    context={
        'content': 'Mini',
        'classes': 'btn btn-primary btn-sm',
    }
)
large_button = Widget(
    'Large button',
    template='widgets/button.html',
    context={
        'content': 'Special Offer',
        'classes': 'btn btn-primary btn-lg',
    }
)
outline_button = Widget(
    'Outline button',
    template='widgets/button.html',
    context={
        'content': 'Optional',
        'classes': 'btn btn-info-outline',
    }
)
disabled_button = Widget(
    'Disabled button',
    template='widgets/button.html',
    context={
        'content': 'Locked',
        'classes': 'btn btn-primary disabled',
    }
)

primary_feedback_button = Widget(
    'Primary feedback button',
    template='widgets/image.html',
    context={
        'url': static('images/feedback.png'),
        'classes': 'img-responsive',
        'name': 'feedback button',
    },
)

accented_feedback_button = Widget(
    'Accented feedback button',
    template='widgets/image.html',
    context={
        'url': static('images/feedback_accented_dark.png'),
        'classes': 'img-responsive',
        'name': 'feedback button accented',
    },
)

buttons = WidgetGroup(
    'Buttons',
    columns=3,
    widgets=[
        link_button, action_button, secondary_button,
        icon_button, linked_button,
        success_button, info_button, warning_button, danger_button,
        small_button, large_button,
        outline_button, disabled_button,
        primary_feedback_button, accented_feedback_button,
    ]
)

widgets.append(buttons)

label = Widget(
    'Simple label',
    template='widgets/label.html',
    context={
        'content': 'Information',
    }
)
accented_label = Widget(
    'Accented label',
    template='widgets/label.html',
    context={
        'content': 'Information',
        'classes': 'bg-accent',
    }
)
rounded_warning_label = Widget(
    'Rounded warning label',
    template='widgets/label.html',
    context={
        'content': 'Warning!',
        'classes': 'label-pill bg-warning',
    }
)

labels = WidgetGroup(
    'Labels',
    columns=3,
    widgets=[
        label, accented_label, rounded_warning_label,
    ]
)

widgets.append(labels)

speech_bubble_right = Widget(
    'Simple bubble',
    template='widgets/speech-bubble.html',
    context={
        'content': 'arrow left',
    }
)
speech_bubble_left = Widget(
    'Bubble left',
    template='widgets/speech-bubble.html',
    context={
        'content': 'arrow right',
        'arrow': 'right',
    }
)
speech_bubble_top = Widget(
    'Bubble top',
    template='widgets/speech-bubble.html',
    context={
        'content': 'arrow down',
        'arrow': 'down',
    }
)
speech_bubble_bottom = Widget(
    'Bubble bottom',
    template='widgets/speech-bubble.html',
    context={
        'content': 'arrow up',
        'arrow': 'up',
    }
)

speech_bubble_right_responsive = Widget(
    'Bubble right responsive',
    template='widgets/speech-bubble.html',
    context={
        'content': 'arrow left responsive up',
        'arrow': 'left pull-up',
        'responsive_arrow': 'up',
    }
)
speech_bubble_left_responsive = Widget(
    'Bubble left responsive',
    template='widgets/speech-bubble.html',
    context={
        'content': 'arrow right responsive up',
        'arrow': 'right pull-up',
        'responsive_arrow': 'up',

    }
)

speeach_bubbles = WidgetGroup(
    'Speech bubbles',
    columns=3,
    widgets=[
        speech_bubble_right, speech_bubble_left, speech_bubble_top, speech_bubble_bottom,
        speech_bubble_right_responsive, speech_bubble_left_responsive,
    ]
)

widgets.append(speeach_bubbles)

anonymous_avatar = Widget(
    'Anonymous avatar',
    template='widgets/avatar.html',
    context={
        'name': 'Anonymous',
        'image': static('legends/images/anonymous.png'),
    }
)
legend_avatar = Widget(
    'Legend avatar',
    template='widgets/avatar.html',
    context={
        'image': static('legends/images/npc/Coralina.png'),
        'name': 'Coralina Charming',
        'url': '#coralina',
    }
)
small_avatar = Widget(
    'Small avatar',
    template='widgets/avatar.html',
    context={
        'image': static('legends/images/npc/Coralina.png'),
        'name': 'Coralina Charming',
        'url': '#coralina',
        'classes': 'small',
    }
)
large_avatar = Widget(
    'Large avatar',
    template='widgets/avatar.html',
    context={
        'image': static('legends/images/npc/Coralina.png'),
        'name': 'Coralina Charming',
        'url': '#coralina',
        'classes': 'large',
    }
)
cake_avatar = Widget(
    'Cake avatar',
    template='widgets/avatar.html',
    context={
        'name': 'Cake',
        'image': static('styleguide/images/icon_cake.png'),
        'classes': 'bg-main-light',
    }
)
camera_avatar = Widget(
    'Camera avatar',
    template='widgets/avatar.html',
    context={
        'name': 'Camera',
        'image': static('styleguide/images/icon_camera.png'),
        'classes': 'bg-main-light',
    }
)

avatars = WidgetGroup(
    'Avatars',
    columns=3,
    widgets=[
        anonymous_avatar, legend_avatar, small_avatar, large_avatar,
        cake_avatar, camera_avatar
    ]
)

widgets.append(avatars)

horizontal_button_group = Widget(
    'Horizontal buttons',
    template='widgets/buttons.html',
    context={
        'buttons': [
            {
                'content': 'Button 1',
                'classes': 'btn btn-primary',
            },
            {
                'content': 'Button 2',
                'classes': 'btn btn-primary',
            },
            {
                'content': 'Button 3',
                'classes': 'btn btn-primary',
            },
        ],
    }
)
small_button_group = Widget(
    'Small buttons',
    template='widgets/buttons.html',
    context={
        'buttons': [
            {
                'content': 'Button 1',
                'classes': 'btn btn-primary',
            },
            {
                'content': 'Button 2',
                'classes': 'btn btn-primary',
            },
            {
                'content': 'Button 3',
                'classes': 'btn btn-primary',
            },
        ],
        'classes': 'btn-group btn-group-sm',
    }
)
small_vertical_button_group = Widget(
    'Small vertical buttons',
    template='widgets/buttons.html',
    context={
        'buttons': [
            {
                'content': 'Button 1',
                'classes': 'btn btn-primary',
            },
            {
                'content': 'Button 2',
                'classes': 'btn btn-primary',
            },
            {
                'content': 'Button 3',
                'classes': 'btn btn-primary',
            },
        ],
        'classes': 'btn-group-vertical',
    }
)

button_groups = WidgetGroup(
    'Button groups',
    columns=12,
    widgets=[
        horizontal_button_group, small_button_group, small_vertical_button_group,
    ]
)

widgets.append(button_groups)

action_menu = Widget(
    'Action menu',
    template='widgets/action-menu.html',
    context={
        'actions': [
            {
                'name': 'Action 1',
                'url': '#action1',
            },
            {
                'name': 'Action 2',
                'url': '#action2',
            },
            {
                'name': 'Action 3',
                'url': '#action3',
            },
        ],
    }
)

action_menu_right = Widget(
    'Right action menu',
    template='widgets/action-menu.html',
    context={
        'actions': [
            {
                'name': 'detail',
                'url': '#action3',
            },
            {
                'name': 'update',
                'url': '#action1',
            },
            {
                'name': 'delete',
                'url': '#action2',
            },
        ],
        'right': True,
        'classes': 'pull-right'
    }
)

button_groups = WidgetGroup(
    'Action menus',
    columns=6,
    widgets=[
        action_menu, action_menu_right,
    ]
)

widgets.append(button_groups)

legend = Widget(
    'Legend',
    template='legends/widgets/legend.html',
    context={
        'avatar': legend_avatar.render(),
        'link': link_legend.render(),
    }
)

legend_large = Widget(
    'Legend large',
    template='legends/widgets/legend.html',
    context={
        'avatar': large_avatar.render(),
        'link': link_legend.render(),
    }
)

legend_small = Widget(
    'Legend large',
    template='legends/widgets/legend.html',
    context={
        'avatar': small_avatar.render(),
        'link': link_legend.render(),
    }
)

legends = WidgetGroup(
    'Legends',
    columns=4,
    widgets=[
        legend, legend_large, legend_small,
    ]
)

widgets.append(legends)

statement_left = Widget(
    'Left statement',
    template='widgets/statement.html',
    context={
        'speaker': legend.render(),
        'content': speech_bubble_right_responsive.render(),
        'speaker_classes': 'col-sm-4',
        'bubble_classes': 'col-sm-8',
    },
    columns=8,
)

statement_right = Widget(
    'Right statement',
    template='widgets/statement.html',
    context={
        'speaker': legend.render(),
        'content': speech_bubble_left_responsive.render(),
        'speaker_classes': 'col-sm-4 col-sm-push-8',
        'bubble_classes': 'col-sm-8  col-sm-pull-4',
    },
    columns=8,
)

statement_big = Widget(
    'Big statement',
    template='widgets/statement.html',
    context={
        'speaker': legend_large.render(),
        'content': speech_bubble_right_responsive.render(),
        'speaker_classes': 'col-sm-4',
        'bubble_classes': 'col-sm-8',
    },
)

statement_small = Widget(
    'Small statement',
    template='widgets/statement.html',
    context={
        'speaker': legend_small.render(),
        'content': speech_bubble_right_responsive.render(),
        'speaker_classes': 'col-sm-4',
        'bubble_classes': 'col-sm-8',
    },
    columns=6
)

statements = WidgetGroup(
    'Statements',
    widgets=[
        statement_left, statement_right, statement_big, statement_small,
    ]
)

widgets.append(statements)

simple_outcome = Widget(
    'Simple outcome',
    template='outcomes/widgets/card.html',
    context={
        'name': 'dummy outcome',
        'status': 0,
        'actions': [
            {
                'name': 'update',
                'url': '#action1',
            },
            {
                'name': 'delete',
                'url': '#action2',
            },
        ],
    },
)

full_outcome = Widget(
    'Full outcome',
    template='outcomes/widgets/card.html',
    context={
        'name': 'garage is clean',
        'description': 'This is my outcome description.\nSecond line.',
        'status': 1,
        'inbox': True,
        'review': 0,
        'date': timezone.now().today(),
        'deadline': timezone.datetime(2020, 1, 7).date(),
        'estimate': timezone.timedelta(days=4),
        'actions': [
            {
                'name': 'update',
                'url': '#action1',
            },
            {
                'name': 'delete',
                'url': '#action2',
            },
        ],

    },
)

outcomes = WidgetGroup(
    'Outcomes',
    columns=6,
    widgets=[
        simple_outcome, full_outcome,
    ]
)

widgets.append(outcomes)

simple_card = Widget(
    'Simple card',
    template='widgets/card.html',
    context={
        'content': 'Hello World',
    }
)
card_with_title = Widget(
    'Card with title',
    template='widgets/card.html',
    context={
        'title': {
            'content': 'Hello',
        },
        'content': 'Hello World',
    }
)
card_with_header = Widget(
    'Card with header',
    template='widgets/card.html',
    context={
        'header': {
            'content': 'Hello above',
        },
        'content': 'Hello World',
    }
)
card_with_footer = Widget(
    'Card with footer',
    template='widgets/card.html',
    context={
        'footer': {
            'content': 'Hello below',
        },
        'content': 'Hello World',
    }
)
dismissable_card = Widget(
    'Dismissable card',
    template='widgets/card.html',
    context={
        'closeable': True,
        'content': 'Close me!',
    }
)
full_card = Widget(
    'Full card',
    template='widgets/card.html',
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

cards = WidgetGroup(
    'Cards',
    columns=6,
    widgets=[
        simple_card, card_with_title, card_with_header, card_with_footer, dismissable_card, full_card,
    ]
)

widgets.append(cards)

anonymous_navigation_bar = Widget(
    'Anonymous navigation bar',
    template='widgets/navbar.html',
    context={
        'id': 'anonymous-bar',
        'menu_id': 'styleguide',
        'classes': 'bg-main-dark',
        'user': AnonymousUser(),
    }
)
legend_navigation_bar = Widget(
    'Legend navigation bar',
    template='widgets/navbar.html',
    context={
        'id': 'legend-bar',
        'menu_id': 'styleguide',
        'classes': 'bg-main-dark',
        'user': AnonymousUser(),
    }
)

navigations = WidgetGroup(
    'Navigations',
    columns=12,
    widgets=[
        anonymous_navigation_bar, legend_navigation_bar,
    ]
)

widgets.append(navigations)

simple_header = Widget(
    'Simple header',
    template='widgets/header.html',
    context={
        'title': 'Page Title Test',
    }
)

full_header = Widget(
    'Header with breadcrumbs links and controls',
    template='widgets/header.html',
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
                'content': 'Link 1',
                'classes': 'btn btn-link',
            },
            {
                'content': 'Link 2',
                'classes': 'btn btn-link',
            },
            {
                'content': 'Link 3',
                'classes': 'btn btn-link',
            },
        ],
        'buttons': [
            {
                'content': 'Button 1',
                'classes': 'btn btn-primary',
            },
            {
                'content': 'Button 2',
                'classes': 'btn btn-primary',
            },
            {
                'content': 'Button 3',
                'classes': 'btn btn-primary',
            },
        ],
    }
)

headers = WidgetGroup(
    'Headers',
    columns=12,
    widgets=[
        simple_header, full_header,
    ]
)

widgets.append(headers)
