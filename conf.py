# -*- coding: utf-8 -*-

import alagitpull

alagitpull.projects = [
    {
        'name': 'Dehaze',
        'url': 'https://github.com/clarkzjw/Dehaze'
    },
    {
        'name': 'GuidedFilter',
        'url': 'https://github.com/clarkzjw/GuidedFilter',
    },
    {
        'name': 'LumberJack',
        'url': 'https://github.com/clarkzjw/LumberJack',
    },
    {
        'name': 'one-two-three...infinity',
        'url': 'https://github.com/clarkzjw/one-two-three...infinity'
    },
    {
        'name': 'nginx-proxy-google',
        'url': 'https://github.com/clarkzjw/nginx-proxy-google',
    },
    {
        'name': 'brainfuck',
        'url': 'https://github.com/clarkzjw/brainfuck'
    }
]

extensions = [
    'sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.intersphinx',
    'sphinx.ext.todo', 'sphinx.ext.viewcode', 'alagitpull'
]

html_title = 'Hello World'
language='zh-Hans-CN'
templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'ring0.xyz'
copyright = u'2013 - 2018, clarkzjw'  # NOQA

version = '0.0'
release = '0.0'

exclude_patterns = ['_build', '.venv', 'README.rst']

pygments_style = 'sphinx'

html_theme_path = [alagitpull.get_path()]
html_theme = 'alagitpull'
html_favicon = '_static/favicon.ico'
html_theme_options = {
    'logo': 'img/terminal-icon.png',
    'projects': alagitpull.projects,
}
html_sidebars = {
    '**': [
        'about.html',
        'relations.html',
        'more.html',
    ]
}

html_static_path = ['_static']

htmlhelp_basename = 'confuciangentlemansclubdoc'

latex_elements = {
}

latex_documents = [
    ('index', 'confuciangentlemansclub.tex', u'confucian gentleman\'s', 'manual'),
]

man_pages = [
    ('index', 'confuciangentlemansclub', u'confucian gentleman\'s club', 1)
]

texinfo_documents = [
    ('index', 'confuciangentlemansclub', u'confucian gentleman\'s club', 'confuciangentlemansclub', 'Scribe.',
     'Miscellaneous'),
]
