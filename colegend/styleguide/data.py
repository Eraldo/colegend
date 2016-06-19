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
        tag='heading',
        libraries='core_tags',
        parameters={
            'content': 'Heading widget example as tag with comments',
            'level': 4,
        },
        comment='Help foo\nbla',
    )
)

widgets.append(
    WidgetGroup(
        'Logos',
        columns=4,
        widgets=[
            Widget(
                'Default',
                template='widgets/div.html',
                context={
                    'content': image(static('images/coLegendLogo_86x18.png'), name='logo'),
                    'classes': 'card-block',
                }
            ),
            Widget(
                'Default',
                template='widgets/div.html',
                context={
                    'content': image(static('images/coLegendLogo_white_86x18.png'), name='logo inverted'),
                    'classes': 'card-block bg-main-dark',
                }
            ),
            Widget(
                'favicon',
                template='widgets/div.html',
                context={
                    'content': image(static('images/favicon.ico'), name='favicon'),
                    'classes': 'card-block',
                }
            ),
        ]
    )
)

widgets.append(
    WidgetGroup(
        'Colors',
        columns=12,
        widgets=[
            WidgetGroup(
                'Project colors',
                columns=4,
                widgets=[
                    Widget(
                        'Main color',
                        template='styleguide/widgets/color.html',
                        context={
                            'name': 'main',
                        }
                    ),
                    Widget(
                        'Main light color',
                        template='styleguide/widgets/color.html',
                        context={
                            'name': 'main-light',
                        }
                    ),
                    Widget(
                        'Main dark color',
                        template='styleguide/widgets/color.html',
                        context={
                            'name': 'main-dark',
                        }
                    ),
                    Widget(
                        'Accent color',
                        template='styleguide/widgets/color.html',
                        context={
                            'name': 'accent',
                        }
                    ),
                    Widget(
                        'Accent light color',
                        template='styleguide/widgets/color.html',
                        context={
                            'name': 'accent-light',
                        }
                    ),
                    Widget(
                        'Accent dark color',
                        template='styleguide/widgets/color.html',
                        context={
                            'name': 'accent-dark',
                        }
                    ),
                ]
            ),
            WidgetGroup(
                'Catagory colors',
                columns=4,
                widgets=[
                    Widget(
                        'Catagrory 1 color',
                        template='styleguide/widgets/color.html',
                        context={
                            'name': 'category-1',
                        }
                    ),
                    Widget(
                        'Catagrory 2 color',
                        template='styleguide/widgets/color.html',
                        context={
                            'name': 'category-2',
                        }
                    ),
                    Widget(
                        'Catagrory 3 color',
                        template='styleguide/widgets/color.html',
                        context={
                            'name': 'category-3',
                        }
                    ),
                    Widget(
                        'Catagrory 4 color',
                        template='styleguide/widgets/color.html',
                        context={
                            'name': 'category-4',
                        }
                    ),
                    Widget(
                        'Catagrory 5 color',
                        template='styleguide/widgets/color.html',
                        context={
                            'name': 'category-5',
                        }
                    ),
                    Widget(
                        'Catagrory 6 color',
                        template='styleguide/widgets/color.html',
                        context={
                            'name': 'category-6',
                        }
                    ),
                    Widget(
                        'Catagrory 7 color',
                        template='styleguide/widgets/color.html',
                        context={
                            'name': 'category-7',
                        }
                    ),
                ]
            ),
            WidgetGroup(
                'Action colors',
                columns=4,
                widgets=[
                    Widget(
                        'Primary color',
                        template='styleguide/widgets/color.html',
                        context={
                            'name': 'primary',
                        }
                    ),
                    Widget(
                        'Success color',
                        template='styleguide/widgets/color.html',
                        context={
                            'name': 'success',
                        }
                    ),
                    Widget(
                        'Info color',
                        template='styleguide/widgets/color.html',
                        context={
                            'name': 'info',
                        }
                    ),
                    Widget(
                        'Warning color',
                        template='styleguide/widgets/color.html',
                        context={
                            'name': 'warning',
                        }
                    ),
                    Widget(
                        'Danger color',
                        template='styleguide/widgets/color.html',
                        context={
                            'name': 'danger',
                        }
                    ),
                ]
            ),
        ]
    ),
)

widgets.append(
    WidgetGroup(
        'Headings',
        columns=12,
        widgets=[
            TagWidget(
                'Heading 1',
                tag='heading',
                parameters={
                    'content': 'Heading Level 1',
                }
            ),
            Widget(
                'Heading 2',
                template='widgets/heading.html',
                context={
                    'content': 'Heading Level 2',
                    'level': 2,
                }
            ),
            Widget(
                'Heading 3',
                template='widgets/heading.html',
                context={
                    'content': 'Heading Level 3',
                    'level': 3,
                }
            ),
            Widget(
                'Heading 4',
                template='widgets/heading.html',
                context={
                    'content': 'Heading Level 4',
                    'level': 4,
                }
            ),
            Widget(
                'Heading 5',
                template='widgets/heading.html',
                context={
                    'content': 'Heading Level 5',
                    'level': 5,
                }
            ),
            Widget(
                'Heading 6',
                template='widgets/heading.html',
                context={
                    'content': 'Heading Level 6',
                    'level': 6,
                }
            ),
        ]
    )
)

widgets.append(
    WidgetGroup(
        'Links',
        columns=4,
        widgets=[
            TagWidget(
                'Simple link',
                tag='link',
                parameters={
                    'content': 'foo bar',
                    'url': '#foobar',
                }
            ),
            Widget(
                'External link',
                template='widgets/link.html',
                context={
                    'content': 'google',
                    'url': 'http://www.google.com',
                    'external': True,
                }
            ),
            Widget(
                'Legend link',
                template='widgets/link.html',
                context={
                    'content': 'Coralina',
                    'url': '#coralina',
                }
            ),
        ]
    )
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

widgets.append(
    WidgetGroup(
        'Buttons',
        columns=3,
        widgets=[
            TagWidget(
                'Link button',
                tag='button',
                parameters={
                    'name': 'Link',
                    'classes': 'btn-link',
                }
            ),
            Widget(
                'Action button',
                template='widgets/button.html',
                context={
                    'content': 'Action',
                    'classes': 'btn btn-primary',
                }
            ),
            Widget(
                'Secondary button',
                template='widgets/button.html',
                context={
                    'content': 'Secondary',
                    'classes': 'btn btn-secondary',
                }
            ),
            Widget(
                'Button with icon',
                template='widgets/button.html',
                context={
                    'content': format_html('{} {}', Widget.get('Challenges icon'), 'Star'),
                    'classes': 'btn btn-primary',
                }
            ),
            Widget(
                'Button with link',
                template='widgets/button.html',
                context={
                    'content': 'Click Me',
                    'classes': 'btn btn-primary',
                    'url': 'https://www.google.com',
                }
            ),
            Widget(
                'Success button',
                template='widgets/button.html',
                context={
                    'content': 'Yeah!',
                    'classes': 'btn btn-success',
                }
            ),
            Widget(
                'Info button',
                template='widgets/button.html',
                context={
                    'content': 'More info',
                    'classes': 'btn btn-info',
                }
            ),
            Widget(
                'Warning button',
                template='widgets/button.html',
                context={
                    'content': 'Caution',
                    'classes': 'btn btn-warning',
                }
            ),
            Widget(
                'Danger button',
                template='widgets/button.html',
                context={
                    'content': 'Delete',
                    'classes': 'btn btn-danger',
                }
            ),
            Widget(
                'Small button',
                template='widgets/button.html',
                context={
                    'content': 'Mini',
                    'classes': 'btn btn-primary btn-sm',
                }
            ),
            Widget(
                'Large button',
                template='widgets/button.html',
                context={
                    'content': 'Special Offer',
                    'classes': 'btn btn-primary btn-lg',
                }
            ),
            Widget(
                'Outline button',
                template='widgets/button.html',
                context={
                    'content': 'Optional',
                    'classes': 'btn btn-info-outline',
                }
            ),
            Widget(
                'Disabled button',
                template='widgets/button.html',
                context={
                    'content': 'Locked',
                    'classes': 'btn btn-primary disabled',
                }
            ),
            Widget(
                'Primary feedback button',
                template='widgets/image.html',
                context={
                    'url': static('images/feedback.png'),
                    'classes': 'img-responsive',
                    'name': 'feedback button',
                },
            ),
            Widget(
                'Accented feedback button',
                template='widgets/image.html',
                context={
                    'url': static('images/feedback_accented_dark.png'),
                    'classes': 'img-responsive',
                    'name': 'feedback button accented',
                },
            ),
        ]
    )
)

widgets.append(
    WidgetGroup(
        'Labels',
        columns=3,
        widgets=[
            TagWidget(
                'Simple label',
                tag='label',
                parameters={
                    'content': 'Information',
                }
            ),
            Widget(
                'Accented label',
                template='widgets/label.html',
                context={
                    'content': 'Information',
                    'classes': 'bg-accent',
                }
            ),
            Widget(
                'Rounded warning label',
                template='widgets/label.html',
                context={
                    'content': 'Warning!',
                    'classes': 'label-pill bg-warning',
                }
            ),
        ]
    )
)

widgets.append(
    WidgetGroup(
        'Speech bubbles',
        columns=3,
        widgets=[
            TagWidget(
                'Bubble',
                tag='speech_bubble',
                parameters={
                    'content': 'arrow left',
                }
            ),
            Widget(
                'Bubble left',
                template='widgets/speech-bubble.html',
                context={
                    'content': 'arrow right',
                    'arrow': 'right',
                }
            ),
            Widget(
                'Bubble top',
                template='widgets/speech-bubble.html',
                context={
                    'content': 'arrow down',
                    'arrow': 'down',
                }
            ),
            Widget(
                'Bubble bottom',
                template='widgets/speech-bubble.html',
                context={
                    'content': 'arrow up',
                    'arrow': 'up',
                }
            ),
            Widget(
                'Bubble right responsive',
                template='widgets/speech-bubble.html',
                context={
                    'content': 'arrow left responsive up',
                    'arrow': 'left pull-up',
                    'responsive_arrow': 'up',
                }
            ),
            Widget(
                'Bubble left responsive',
                template='widgets/speech-bubble.html',
                context={
                    'content': 'arrow right responsive up',
                    'arrow': 'right pull-up',
                    'responsive_arrow': 'up',

                }
            ),
        ]
    )
)

widgets.append(
    WidgetGroup(
        'Avatars',
        columns=3,
        widgets=[
            Widget(
                'Anonymous avatar',
                template='widgets/avatar.html',
                context={
                    'name': 'Anonymous',
                    'image': static('legends/images/anonymous.png'),
                }
            ),
            Widget(
                'Legend avatar',
                template='widgets/avatar.html',
                context={
                    'image': static('legends/images/npc/Coralina.png'),
                    'name': 'Coralina Charming',
                    'url': '#coralina',
                }
            ),
            Widget(
                'Small avatar',
                template='widgets/avatar.html',
                context={
                    'image': static('legends/images/npc/Coralina.png'),
                    'name': 'Coralina Charming',
                    'url': '#coralina',
                    'classes': 'small',
                }
            ),
            Widget(
                'Large avatar',
                template='widgets/avatar.html',
                context={
                    'image': static('legends/images/npc/Coralina.png'),
                    'name': 'Coralina Charming',
                    'url': '#coralina',
                    'classes': 'large',
                }
            ),
            Widget(
                'Cake avatar',
                template='widgets/avatar.html',
                context={
                    'name': 'Cake',
                    'image': static('styleguide/images/icon_cake.png'),
                    'classes': 'bg-main-light',
                }
            ),
            Widget(
                'Camera avatar',
                template='widgets/avatar.html',
                context={
                    'name': 'Camera',
                    'image': static('styleguide/images/icon_camera.png'),
                    'classes': 'bg-main-light',
                }
            ),
        ]
    )
)

widgets.append(
    WidgetGroup(
        'Button groups',
        columns=12,
        widgets=[
            Widget(
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
            ),
            Widget(
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
            ),
            Widget(
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
            ),
        ]
    )
)

widgets.append(
    WidgetGroup(
        'Action menus',
        columns=6,
        widgets=[
            Widget(
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
            ),
            Widget(
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
            ),
        ]
    )
)

widgets.append(
    WidgetGroup(
        'Legends',
        columns=4,
        widgets=[
            Widget(
                'Legend',
                template='legends/widgets/legend.html',
                context={
                    'avatar': Widget.get('Legend avatar'),
                    'link': Widget.get('Legend link'),
                }
            ),
            Widget(
                'Legend large',
                template='legends/widgets/legend.html',
                context={
                    'avatar': Widget.get('Large avatar'),
                    'link': Widget.get('Legend link'),
                }
            ),
            Widget(
                'Legend small',
                template='legends/widgets/legend.html',
                context={
                    'avatar': Widget.get('Small avatar'),
                    'link': Widget.get('Legend link'),
                }
            ),
        ]
    )
)

widgets.append(
    WidgetGroup(
        'Statements',
        widgets=[
            Widget(
                'Left statement',
                template='widgets/statement.html',
                context={
                    'speaker': Widget.get('Legend'),
                    'content': Widget.get('Bubble right responsive'),
                    'speaker_classes': 'col-sm-4',
                    'bubble_classes': 'col-sm-8',
                },
                columns=8,
            ),
            Widget(
                'Right statement',
                template='widgets/statement.html',
                context={
                    'speaker': Widget.get('Legend'),
                    'content': Widget.get('Bubble left responsive'),
                    'speaker_classes': 'col-sm-4 col-sm-push-8',
                    'bubble_classes': 'col-sm-8  col-sm-pull-4',
                },
                columns=8,
            ),
            Widget(
                'Big statement',
                template='widgets/statement.html',
                context={
                    'speaker': Widget.get('Legend large'),
                    'content': Widget.get('Bubble right responsive'),
                    'speaker_classes': 'col-sm-4',
                    'bubble_classes': 'col-sm-8',
                },
            ),
            Widget(
                'Small statement',
                template='widgets/statement.html',
                context={
                    'speaker': Widget.get('Legend small'),
                    'content': Widget.get('Bubble right responsive'),
                    'speaker_classes': 'col-sm-4',
                    'bubble_classes': 'col-sm-8',
                },
                columns=6
            ),
        ]
    )
)

widgets.append(
    WidgetGroup(
        'Outcomes',
        columns=6,
        widgets=[
            Widget(
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
            ),
            Widget(
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
            ),
        ]
    )
)

widgets.append(
    WidgetGroup(
        'Cards',
        columns=6,
        widgets=[
            Widget(
                'Simple card',
                template='widgets/card.html',
                context={
                    'content': 'Hello World',
                }
            ),
            Widget(
                'Card with title',
                template='widgets/card.html',
                context={
                    'title': {
                        'content': 'Hello',
                    },
                    'content': 'Hello World',
                }
            ),
            Widget(
                'Card with header',
                template='widgets/card.html',
                context={
                    'header': {
                        'content': 'Hello above',
                    },
                    'content': 'Hello World',
                }
            ),
            Widget(
                'Card with footer',
                template='widgets/card.html',
                context={
                    'footer': {
                        'content': 'Hello below',
                    },
                    'content': 'Hello World',
                }
            ),
            Widget(
                'Dismissable card',
                template='widgets/card.html',
                context={
                    'closeable': True,
                    'content': 'Close me!',
                }
            ),
            Widget(
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
            ),
        ]
    )
)

widgets.append(
    WidgetGroup(
        'Navigations',
        columns=12,
        widgets=[
            Widget(
                'Anonymous navigation bar',
                template='widgets/navbar.html',
                context={
                    'id': 'anonymous-bar',
                    'menu_id': 'styleguide',
                    'classes': 'bg-main-dark',
                    'user': AnonymousUser(),
                }
            ),
            Widget(
                'Legend navigation bar',
                template='widgets/navbar.html',
                context={
                    'id': 'legend-bar',
                    'menu_id': 'styleguide',
                    'classes': 'bg-main-dark',
                    'user': AnonymousUser(),
                }
            ),
        ]
    )
)

widgets.append(
    WidgetGroup(
        'Headers',
        columns=12,
        widgets=[
            Widget(
                'Simple header',
                template='widgets/header.html',
                context={
                    'title': 'Page Title Test',
                }
            ),
            Widget(
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
            ),
        ]
    )
)
