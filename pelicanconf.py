#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Teren Bryson'
SITENAME = 'cloudsacked.com'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Added by Teren
THEME = "../pelican-themes/flex"
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['sitemap']
TYPOGRIFY = True

SITEMAP = { 
        'format': 'xml', 
        'priorities': { 
            'articles': 1, 
            'indexes': 0.5, 
            'pages': 0.5, 
            }, 
        'changefreqs': { 
            'articles': 'always', 
            'indexes': 'hourly', 
            'pages': 'monthly' 
            }
        }
