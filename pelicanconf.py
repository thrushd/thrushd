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

# theme and theme options
THEME = "../pelican-themes/Flex"
SITELOGO = 'images/bird-logo.png'
SITETITLE = 'Dylan Thrush'
MAIN_MENU = True
MENUITEMS = (('adventure', '/category/adventure.html'), ('projects', '/category/projects.html'))

# plugins
PLUGIN_PATH = '../pelican-plugins'
# PLUGINS = ['a-plugin']

# feed generation is super lame
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
