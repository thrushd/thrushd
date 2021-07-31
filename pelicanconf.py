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
THEME = '../pelican-themes/Flex'
SITELOGO = '/extra/bird-logo.png'
FAVICON = '/extra/favicon.ico'
SITETITLE = 'Dylan Thrush'
MAIN_MENU = True
MENUITEMS = [
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
    ('Archives', '/archives.html')
]

LINKS = [
    ('Contact', 'https://mailhide.io/e/Qcpcib95')
]

SOCIAL = [
    ('github', 'https://github.com/thrushd')
]

STATIC_PATHS = [
    'images',
    'extra',
]

# tell it where it is
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}

CUSTOM_CSS = 'static/custom.css'

# plugins
PLUGIN_PATHS = [
    '../pelican-plugins'
]
PLUGINS = [

]

# feed generation is super lame and I hate it
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
