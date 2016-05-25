import datetime

from django.core.exceptions import ValidationError
from test_plus.test import TestCase

from colegend.core.intuitive_duration2.utils import parse_intuitive_duration, intuitive_duration_string


class TestIntuitiveDuration(TestCase):
    def setUp(self):
        pass

    def test_parse_intuitive_duration(self):
        # Valid input

        valid_input_map = [
            ('40m', datetime.timedelta(minutes=40)),
            ('1h', datetime.timedelta(hours=1)),
            ('3d', datetime.timedelta(days=3)),
            ('2w', datetime.timedelta(weeks=2)),
            ('6M', datetime.timedelta(days=6 * 30)),
            ('1.5h', datetime.timedelta(hours=1.5)),
        ]
        for string, duration in valid_input_map:
            parsed_duration = parse_intuitive_duration(string)
            assert parsed_duration == duration, '{} could not be parsed to {}'.format(repr(string), repr(duration))

        # Invalid input
        invalid_inputs = [
            '1x', 'y', 'd', '9', '1,3d', '1:2h', '1/2h'
        ]

        for string in invalid_inputs:
            self.assertRaises(ValidationError, parse_intuitive_duration, string)

    def test_intuitive_duration_string(self):
        # Valid input
        assert intuitive_duration_string(datetime.timedelta(minutes=40)) == '40m'
        assert intuitive_duration_string(datetime.timedelta(hours=1)) == '1h'
        assert intuitive_duration_string(datetime.timedelta(days=3)) == '3d'
        assert intuitive_duration_string(datetime.timedelta(weeks=2)) == '2w'
        assert intuitive_duration_string(datetime.timedelta(days=180)) == '6M'
        assert intuitive_duration_string(datetime.timedelta(hours=1, minutes=30)) == '1.5h'
        # Invalid input
        self.assertRaises(ValidationError, intuitive_duration_string, '1h')
