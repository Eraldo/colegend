from django.core.validators import RegexValidator


class MonthValidator(RegexValidator):
    regex='^\d{4}-W\d{2}$',
    message='Month format must look like this: "2016-W02" for year: 2016, month number: 2',
    code='invalid_month_format'

