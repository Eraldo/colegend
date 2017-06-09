from calendar import monthrange
from math import ceil

import datetime
from django.utils import timezone
from django.utils.dateparse import parse_date


class Scope:
    def __init__(self, date=None):
        if date:
            if isinstance(date, str):
                date = parse_date(date) or self.parse_date(date)
            elif isinstance(date, datetime.date):
                pass
            else:
                raise ValueError('Provided date is not in a valid format.')
        else:
            date = timezone.localtime(timezone.now()).date()
        self.date = date

    def parse_date(self, string):
        raise NotImplementedError

    @property
    def name(self):
        return self.__class__.__name__.lower()

    @property
    def day(self):
        return Day(date=self.date)

    @property
    def week(self):
        return Week(date=self.date)

    @property
    def month(self):
        return Month(date=self.date)

    @property
    def quarter(self):
        return Quarter(date=self.date)

    @property
    def year(self):
        return Year(date=self.date)

    @property
    def start(self):
        raise NotImplementedError

    @property
    def end(self):
        raise NotImplementedError

    @property
    def range(self):
        return self.start, self.end

    @property
    def display(self):
        return str(self)


class Day(Scope):
    def parse_date(self, string):
        return timezone.datetime.strptime(string, "%Y-%m-%d").date()

    @property
    def delta(self):
        return timezone.timedelta(days=1)

    @property
    def start(self):
        return self.date

    @property
    def end(self):
        return self.date

    @property
    def previous(self):
        date = self.date - self.delta
        return self.__class__(date=date)

    @property
    def next(self):
        date = self.date + self.delta
        return self.__class__(date=date)

    def __str__(self):
        return str(self.date)


class Week(Scope):
    def parse_date(self, string):
        return timezone.datetime.strptime('{}-1'.format(string), "%Y-W%W-%w").date()

    @property
    def delta(self):
        return timezone.timedelta(days=7)

    @property
    def start(self):
        date = self.date
        return date - timezone.timedelta(days=date.weekday())

    @property
    def end(self):
        return self.start + timezone.timedelta(days=6)

    @property
    def previous(self):
        date = self.date - self.delta
        return self.__class__(date=date)

    @property
    def next(self):
        date = self.date + self.delta
        return self.__class__(date=date)

    @property
    def number(self):
        return self.date.isocalendar()[1]

    def __str__(self):
        year = self.start.year # .date.year is not enough since the week number can be of the previous year
        return '{year}-W{week:02d}'.format(year=year, week=self.number)


class Month(Scope):
    def parse_date(self, string=None):
        return timezone.datetime.strptime('{}'.format(string), "%Y-M%m").date()

    @property
    def delta(self):
        date = self.date
        days = monthrange(date.year, date.month)[1]
        return timezone.timedelta(days=days)

    @property
    def start(self):
        date = self.date
        year, month, day = date.year, date.month, date.day
        return timezone.datetime(year, month, 1).date()

    @property
    def end(self):
        return self.start + self.delta - timezone.timedelta(days=1)

    @property
    def previous(self):
        # last day of previous month
        last_day = self.start - timezone.timedelta(days=1)
        # first day of previous month
        first_day = timezone.datetime(year=last_day.year, month=last_day.month, day=1).date()
        return self.__class__(date=first_day)

    @property
    def next(self):
        date = self.end + timezone.timedelta(days=1)
        return self.__class__(date=date)

    @property
    def number(self):
        return self.date.month

    def __str__(self):
        date = self.date
        return '{year}-M{month:02d}'.format(year=date.year, month=self.number)


class Quarter(Scope):
    quarter_months = {
        1: 1,
        2: 4,
        3: 7,
        4: 10,
    }

    def parse_date(self, string):
        year, quarter = map(int, string.split('-Q'))
        return timezone.datetime(year=year, month=self.quarter_months.get(quarter), day=1).date()

    @property
    def delta(self):
        return self.end - self.start

    @property
    def start(self):
        return timezone.datetime(self.date.year, self.quarter_months.get(self.number), 1).date()

    @property
    def end(self):
        return Month(date=self.start).next.next.end

    @property
    def previous(self):
        # last day of previous month
        last_day = self.start - timezone.timedelta(days=1)
        # first day of previous month
        first_day = timezone.datetime(year=last_day.year, month=last_day.month, day=1).date()
        return self.__class__(date=first_day)

    @property
    def next(self):
        date = self.end + timezone.timedelta(days=1)
        return self.__class__(date=date)

    @property
    def number(self):
        return int(ceil(self.date.month / 3.))

    def __str__(self):
        date = self.date
        return '{year}-Q{quarter}'.format(year=date.year, quarter=self.number)


class Year(Scope):
    def parse_date(self, string):
        return timezone.datetime(year=int(string), month=1, day=1).date()

    @property
    def start(self):
        return timezone.datetime(year=self.number, month=1, day=1).date()

    @property
    def end(self):
        return self.next.date - timezone.timedelta(days=1)

    @property
    def previous(self):
        date = timezone.datetime(year=self.number - 1, month=1, day=1).date()
        return self.__class__(date=date)

    @property
    def next(self):
        date = timezone.datetime(year=self.number + 1, month=1, day=1).date()
        return self.__class__(date=date)

    @property
    def number(self):
        return self.date.year

    def __str__(self):
        return '{year}'.format(year=self.number)


all = [Day, Week, Month, Quarter, Year]
