# -*- coding: utf-8 -*-
# Data for the styleguide context

atoms = [
    {
        'name': 'Project Colors',
        'template': 'styleguide/molecules/atoms.html',
        'context': {
            'columns': 4,
            'atoms': [
                {
                    'name': 'Main',
                    'template': 'styleguide/atoms/color.html',
                    'context': {
                        'name': 'main',
                        'code': '#26C6DA',
                    },
                },
                {
                    'name': 'Main light',
                    'template': 'styleguide/atoms/color.html',
                    'context': {
                        'name': 'main-light',
                        'code': '#B2EBF2',
                    },
                },
                {
                    'name': 'Main dark',
                    'template': 'styleguide/atoms/color.html',
                    'context': {
                        'name': 'main-dark',
                        'code': '#0097A7',
                    },
                },
                {
                    'name': 'Accent',
                    'template': 'styleguide/atoms/color.html',
                    'context': {
                        'name': 'accent',
                        'code': '#9CCC65',
                    },
                },
                {
                    'name': 'Accent light',
                    'template': 'styleguide/atoms/color.html',
                    'context': {
                        'name': 'accent-light',
                        'code': '#DCEDC8',
                    },
                },
                {
                    'name': 'Accent dark',
                    'template': 'styleguide/atoms/color.html',
                    'context': {
                        'name': 'accent-dark',
                        'code': '#689F38',
                    },
                },
            ],
        },
    },
    {
        'name': 'Category Colors',
        'template': 'styleguide/molecules/atoms.html',
        'context': {
            'columns': 3,
            'atoms': [
                {
                    'name': 'Color "category 1"',
                    'template': 'styleguide/atoms/color.html',
                    'context': {
                        'name': 'category-1',
                        'code': '#ED143D',
                    },
                },
                {
                    'name': 'Color "category 2"',
                    'template': 'styleguide/atoms/color.html',
                    'context': {
                        'name': 'category-2',
                        'code': '#FF8C00',
                    },
                },
                {
                    'name': 'Color "category 3"',
                    'template': 'styleguide/atoms/color.html',
                    'context': {
                        'name': 'category-3',
                        'code': '#FFD700',
                    },
                },
                {
                    'name': 'Color "category 4"',
                    'template': 'styleguide/atoms/color.html',
                    'context': {
                        'name': 'category-4',
                        'code': '#008000',
                    },
                },
                {
                    'name': 'Color "category 5"',
                    'template': 'styleguide/atoms/color.html',
                    'context': {
                        'name': 'category-5',
                        'code': '#1E90FF',
                    },
                },
                {
                    'name': 'Color "category 6"',
                    'template': 'styleguide/atoms/color.html',
                    'context': {
                        'name': 'category-6',
                        'code': '#4B0082',
                    },
                },
                {
                    'name': 'Color "category 7"',
                    'template': 'styleguide/atoms/color.html',
                    'context': {
                        'name': 'category-7',
                        'code': '#EE82EE',
                    },
                },
            ],
        },
    },
    {
        'name': 'Action Colors',
        'template': 'styleguide/molecules/atoms.html',
        'context': {
            'columns': 3,
            'atoms': [
                {
                    'name': 'Color "primary"',
                    'template': 'styleguide/atoms/color.html',
                    'context': {
                        'name': 'primary',
                    },
                },
                {
                    'name': 'Color "success"',
                    'template': 'styleguide/atoms/color.html',
                    'context': {
                        'name': 'success',
                    },
                },
                {
                    'name': 'Color "info"',
                    'template': 'styleguide/atoms/color.html',
                    'context': {
                        'name': 'info',
                    },
                },
                {
                    'name': 'Color "warning"',
                    'template': 'styleguide/atoms/color.html',
                    'context': {
                        'name': 'warning',
                    },
                },
                {
                    'name': 'Color "danger"',
                    'template': 'styleguide/atoms/color.html',
                    'context': {
                        'name': 'danger',
                    },
                },
            ],
        },
    },
    {
        'name': 'Headlines',
        'template': 'styleguide/molecules/atoms.html',
        'context': {
            'columns': 12,
            'atoms': [
                {
                    'name': 'Headline 1',
                    'template': 'atoms/headline.html',
                    'context': {
                        'text': 'Heading Level 1',
                    },
                },
                {
                    'name': 'Headline 2',
                    'template': 'atoms/headline.html',
                    'context': {
                        'level': 2,
                        'text': 'Heading Level 2',
                    },
                },
                {
                    'name': 'Headline 3',
                    'template': 'atoms/headline.html',
                    'context': {
                        'level': 3,
                        'text': 'Heading Level 3',
                    },
                },
                {
                    'name': 'Headline 4',
                    'template': 'atoms/headline.html',
                    'context': {
                        'level': 4,
                        'text': 'Heading Level 4',
                    },
                },
                {
                    'name': 'Headline 5',
                    'template': 'atoms/headline.html',
                    'context': {
                        'level': 5,
                        'text': 'Heading Level 5',
                    },
                },
                {
                    'name': 'Headline 6',
                    'template': 'atoms/headline.html',
                    'context': {
                        'level': 6,
                        'text': 'Heading Level 6',
                    },
                },
            ],
        },
    },
    {
        'name': 'Link',
        'template': 'styleguide/atoms/link.html',
        'context': {
        },
    },
    {
        'name': 'Buttons',
        'template': 'styleguide/molecules/atoms.html',
        'context': {
            'columns': 3,
            'atoms': [
                {
                    'name': 'Link button',
                    'template': 'atoms/button.html',
                    'context': {
                        'text': 'Link',
                        'class': 'btn-link',
                    },
                },
                {
                    'name': 'Action button',
                    'template': 'atoms/button.html',
                    'context': {
                        'text': 'Action',
                        'class': 'btn-primary',
                    },
                },
                {
                    'name': 'Secondary button',
                    'template': 'atoms/button.html',
                    'context': {
                        'text': 'Login',
                        'class': 'btn-secondary',
                    },
                },
                {
                    'name': 'Button with icon',
                    'template': 'atoms/button.html',
                    'context': {
                        'text': 'Star',
                        'icon': 'star',
                        'class': 'btn-primary',
                    },
                },
                {
                    'name': 'Button with link',
                    'template': 'atoms/button.html',
                    'context': {
                        'text': 'Click Me',
                        'class': 'btn-primary',
                        'url': 'https://www.google.com',
                    },
                },
                {
                    'name': 'Success button',
                    'template': 'atoms/button.html',
                    'context': {
                        'text': 'Yeah!',
                        'class': 'btn-success',
                    },
                },
                {
                    'name': 'Info button',
                    'template': 'atoms/button.html',
                    'context': {
                        'text': 'More info',
                        'class': 'btn-info',
                    },
                },
                {
                    'name': 'Warning button',
                    'template': 'atoms/button.html',
                    'context': {
                        'text': 'Caution',
                        'class': 'btn-warning',
                    },
                },
                {
                    'name': 'Danger button',
                    'template': 'atoms/button.html',
                    'context': {
                        'text': 'Delete',
                        'class': 'btn-danger',
                    },
                },
                {
                    'name': 'Small button',
                    'template': 'atoms/button.html',
                    'context': {
                        'text': 'Mini',
                        'class': 'btn-primary btn-sm',
                    },
                },
                {
                    'name': 'Large Button',
                    'template': 'atoms/button.html',
                    'context': {
                        'text': 'Special Offer',
                        'class': 'btn-primary btn-lg',
                    },
                },
                {
                    'name': 'Outline button',
                    'template': 'atoms/button.html',
                    'context': {
                        'text': 'Optional',
                        'class': 'btn-info-outline',
                    },
                },
                {
                    'name': 'Disabled button',
                    'template': 'atoms/button.html',
                    'context': {
                        'text': 'Locked',
                        'class': 'btn-primary disabled',
                    },
                },
            ],
        },
    },
    {
        'name': 'Avatars',
        'template': 'styleguide/molecules/atoms.html',
        'context': {
            'columns': 3,
            'atoms': [
                {
                    'name': 'Anonymous avatar',
                    'template': 'atoms/avatar.html',
                    'context': {
                        'image': 'legends/images/anonymous.png',
                    },
                },
                {
                    'name': 'Legend avatar',
                    'template': 'atoms/avatar.html',
                    'context': {
                        'image': 'legends/images/npc/Coralina.png',
                        'name': 'Coralina Charming',
                        'url': '#coralina',
                    },
                },
                {
                    'name': 'Small legend avatar',
                    'template': 'atoms/avatar.html',
                    'context': {
                        'image': 'legends/images/npc/Coralina.png',
                        'name': 'Coralina Charming',
                        'url': '#coralina',
                        'size': 'small',
                    },
                },
                {
                    'name': 'large legend avatar',
                    'template': 'atoms/avatar.html',
                    'context': {
                        'image': 'legends/images/npc/Coralina.png',
                        'name': 'Coralina Charming',
                        'url': '#coralina',
                        'size': 'large',
                    },
                },
            ],
        },
    },
    {
        'name': 'Badges',
        'template': 'styleguide/molecules/atoms.html',
        'context': {
            'columns': 3,
            'atoms': [
                {
                    'name': 'Cake badge',
                    'template': 'atoms/badge.html',
                    'context': {
                        'name': 'Cake',
                        'category': '3',
                        'image': 'styleguide/images/icon_cake.png',
                    },
                },
                {
                    'name': 'Camera badge',
                    'template': 'atoms/badge.html',
                    'context': {
                        'name': 'Camera',
                        'category': '5',
                        'image': 'styleguide/images/icon_camera.png',
                    },
                },
            ],
        },
    },
]

molecules = [
    {
        'name': 'Buttons',
        'template': 'styleguide/molecules/atoms.html',
        'context': {
            'columns': 12,
            'atoms': [
                {
                    'name': 'Button group',
                    'template': 'molecules/buttons.html',
                    'context': {
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
                    },
                },
                {
                    'name': 'Small button group',
                    'template': 'molecules/buttons.html',
                    'context': {
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
                    },
                },
                {
                    'name': 'Small button vertical',
                    'template': 'molecules/buttons.html',
                    'context': {
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
                    },
                },
            ],
        },
    },
]

organisms = [
    {
        'name': 'Navigation bars',
        'template': 'styleguide/molecules/atoms.html',
        'context': {
            'columns': 12,
            'atoms': [
                {
                    'name': 'Anonymous navigation bar',
                    'template': 'organisms/navbar.html',
                    'context': {
                        'id': 'anonymous-bar',
                        'menu_id': 'styleguide',
                        'class': 'bg-main-dark',
                        'user': {
                            'is_authenticated': False,
                        },
                    },
                },
                {
                    'name': 'Legend navigation bar',
                    'template': 'organisms/navbar.html',
                    'context': {
                        'id': 'legend-bar',
                        'menu_id': 'styleguide',
                        'class': 'bg-main',
                    },
                },
            ],
        },
    },
    {
        'name': 'Headers',
        'template': 'styleguide/molecules/atoms.html',
        'context': {
            'columns': 12,
            'atoms': [
                {
                    'name': 'Simple header',
                    'template': 'organisms/header.html',
                    'context': {
                        'title': 'Page Title Test',
                    },
                },
                {
                    'name': 'Header with breadcrumbs links and controls',
                    'template': 'organisms/header.html',
                    'context': {
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
                    },
                },
            ],
        },
    },
]
