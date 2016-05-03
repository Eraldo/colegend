# -*- coding: utf-8 -*-
# Data for the styleguide context

atoms = [
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
    }, {
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
        'name': 'Buttons',
        'template': 'styleguide/molecules/atoms.html',
        'context': {
            'columns': 3,
            'atoms': [
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
        'name': 'Avatar',
        'template': 'atoms/avatar.html',
        'context': {
            'image': 'legends/images/anonymous.png',
        },
    },
]

molecules = {}

organisms = {}
