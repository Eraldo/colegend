# -*- coding: utf-8 -*-
# Data for the styleguide context

atoms_data = [
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
        'name': 'Button',
        'template': 'atoms/button.html',
        'context': {
            'text': 'Join',
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

molecules_data = {}

organisms_data = {}
