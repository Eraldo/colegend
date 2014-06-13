__author__ = 'eraldo'

# settings/local.py - this file is intended to overwrite the general versioned settings on demand

# replace "base" to some other existing config file to use it as a base instead
from .base import *

# overwrite and set new variables below

# [secrets]

# SECURITY WARNING: set this key and keep it secret!
SECRET_KEY = 'your-secure-key-goes-here'

# [misc]

# example variables:
DEBUG = True
ALLOWED_HOSTS = ["localhost"]
MY_OWN_VARIABLE = "some value"