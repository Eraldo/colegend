import datetime

from django.core.exceptions import ValidationError
from test_plus.test import TestCase

from colegend.core.intuitive_duration2.utils import parse_intuitive_duration


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
            '1x',
        ]

        for string in invalid_inputs:
            self.assertRaises(ValidationError, parse_intuitive_duration, string)
            # with pytest.raises(ValidationError):
            #     parsed_duration = parse_intuitive_duration(string)
            # assert parsed_duration == duration, '{} was expected to become {}'.format(repr(string), repr(duration))
