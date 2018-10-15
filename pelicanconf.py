#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

# setup
AUTHOR = 'Dylan Thrush'
SITENAME = 'Dylan Thrush'
SITEURL = 'http://localhost:8000'
PATH = 'content'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

# theme and theme options
THEME = "../pelican-themes/Flex"
SITELOGO = '/extra/bird-logo.png'
FAVICON = '/extra/favicon.ico'
SITETITLE = 'Dylan Thrush'
MAIN_MENU = True
MENUITEMS = (('adventure', '/category/adventure.html'), ('projects', '/category/projects.html'))

STATIC_PATHS = [
    'images',
    'extra',
]


# plugins
PLUGIN_PATH = '../pelican-plugins'
# PLUGINS = ['photos']


# photos config
# PHOTO_LIBRARY = '/images/'
# PHOTO_GALLERY = (1024, 768, 80)
# PHOTO_ARTICLE = (760, 506, 80)
# PHOTO_THUMB = (192, 144, 60)
# PHOTO_SQUARE_THUMB = True
# PHOTO_WATERMARK = False
# PHOTO_EXIF_KEEP = False


# feed generation is super lame
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10


# development
RELATIVE_URLS = True
