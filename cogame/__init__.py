from django.utils.version import get_version

# using same version scheme as django with undefined release cycles
# MAJOR, MINOR, MICRO, STAGE, REVISION]
# http://legacy.python.org/dev/peps/pep-0386/
# https://docs.djangoproject.com/en/1.6/internals/release-process/
VERSION = (0, 1, 0, 'alpha', 1)

__title__ = 'CoGame Project'
# Returns a PEP 386-compliant version number.
__version__ = get_version(VERSION)
__author__ = 'Eraldo Helal'
__copyright__ = 'Copyright 2014 {}'.format(__author__)
