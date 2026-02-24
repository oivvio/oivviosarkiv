#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Oivvio Polite'
SITENAME = u'Oivvios arkiv'
SITEURL = 'https://oivviosarkiv.polite.se'

PATH = 'content'

THEME = './martin-pelican-theme'
TIMEZONE = 'Europe/Stockholm'

DEFAULT_LANG = u'se'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DEFAULT_PAGINATION = 10

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

STATIC_PATHS = ['images', 'pdfs', 'audio', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}
MENUITEMS = [('Hem', '/')]
GOOGLE_ANALYTICS = "UA-2026673-1"

RELATIVE_URLS = False
#RELATIVE_URLS = True
