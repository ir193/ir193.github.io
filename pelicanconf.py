# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ir193'
SITENAME = u'Another Blog'
SITEURL = 'https://ir193.github.io/'
DISQUS_SITENAME = "ir193"
PATH = 'content'

TIMEZONE = 'Asia/Shanghai'
SUMMARY_MAX_LENGTH = 50
DEFAULT_LANG = u'zh-CN'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds/all.rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
ARTICLE_URL = 'post/{slug}.html'
ARTICLE_SAVE_AS = 'post/{slug}.html'
ARTICLE_LANG_SAVE_AS = 'post/{slug}-{lang}.html'
MONTH_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/{date:%b}/index.html'


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
REVERSE_CATEGORY_ORDER = True
SOCIAL = (('github', 'http://github.com/ir193'),)

# global metadata to all the contents
DEFAULT_METADATA = ()

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/.nojykell': {'path': '.nojykell'},
    }


# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'pictures',
    ]

TEMPLATE_PAGES = {}
PLUGINS = {}

