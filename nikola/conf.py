# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
import os

##############################################
# Configuration
##############################################


# Data about this site
BLOG_AUTHOR = "Manuel Kaufmann"
BLOG_TITLE = "Humitos"
# This is the main URL for your site. It will be used
# in a prominent link
SITE_URL = "http://elblogdehumitos.com.ar/"
# This is the URL where nikola's output will be deployed.
# If not set, defaults to SITE_URL
# BASE_URL = "http://nikola.ralsina.com.ar"
BLOG_EMAIL = "humitos@gmail.com"
BLOG_DESCRIPTION = "el blog de Manuel Kaufmann -- comunicando mi vida a la sociedad"

# Nikola is multilingual!
#
# Currently supported languages are:
#   English -> en
#   Greek -> gr
#   German -> de
#   French -> fr
#   Polish -> pl
#   Russian -> ru
#   Spanish -> es
#   Italian -> it
#   Simplified Chinese -> zh-cn
#
# If you want to use Nikola with a non-supported language you have to provide
# a module containing the necessary translations
# (p.e. look at the modules at: ./nikola/data/themes/default/messages/fr.py).
# If a specific post is not translated to a language, then the version
# in the default language will be shown instead.

# What is the default language?
DEFAULT_LANG = "es"

# What other languages do you have?
# The format is {"translationcode" : "path/to/translation" }
# the path will be used as a prefix for the generated pages location
TRANSLATIONS = {
    DEFAULT_LANG: "",
    # Example for another language:
    # "es": "./es",
}

# Links for the sidebar / navigation bar.
# You should provide a key-value pair for each used language.
NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ('/pages/argentina-en-python/', 'Argentina en Python'),
        ('/pages/quien-escribe/', '¿Quién escribe?'),
        ('/pages/traducciones/', 'Traducciones'),
        # ('/pages/modulos-python/', 'Módulos Python'),
        ('http://tutorial.python.org.ar/', 'El Tutorial de Python'),
        (
            (
                ('/pages/apoyo/', 'Apoyo'),
                ('/pages/repositorio/', 'Repositorio'),
                ('/pages/frases/', 'Frases'),
            ),
            'Extras',
        ),
        (
            (
                ('/categories/index.html', 'Etiquetas'),
                ('/archive.html', 'Archivo Anual'),
                ('http://humitos.wordpress.com', 'Viejo Blog en Wordpress'),
            ),
            'Historial',
        ),
        # ('/rss.xml', 'RSS'),
        ('http://feeds.feedburner.com/humitos', 'RSS'),
    ),
}


##############################################
# Below this point, everything is optional
##############################################


# POSTS and PAGES contains (wildcard, destination, template) tuples.
#
# The wildcard is used to generate a list of reSt source files
# (whatever/thing.txt).
#
# That fragment must have an associated metadata file (whatever/thing.meta),
# and opcionally translated files (example for spanish, with code "es"):
#     whatever/thing.txt.es and whatever/thing.meta.es
#
# From those files, a set of HTML fragment files will be generated:
# cache/whatever/thing.html (and maybe cache/whatever/thing.html.es)
#
# These files are combinated with the template to produce rendered
# pages, which will be placed at
# output / TRANSLATIONS[lang] / destination / pagename.html
#
# where "pagename" is specified in the metadata file.
#
# The difference between POSTS and PAGES is that POSTS are added
# to feeds and are considered part of a blog, while PAGES are
# just independent HTML pages.

POSTS = (
    ("posts/nikola/*.rst", "posts", "post.tmpl"),
    # ("posts/wordpress/*.wp", "posts/wordpress", "post.tmpl"),
    ("posts/wordpress/migrated/*.rst", "posts/wordpress", "post.tmpl"),
)

PAGES = (
    ("pages/*.rst", "pages", "story.tmpl"),
)

# One or more folders containing files to be copied as-is into the output.
# The format is a dictionary of "source" "relative destination".
# Default is:
# FILES_FOLDERS = {'files': '' }
# Which means copy 'files' into 'output'

# A mapping of languages to file-extensions that represent that language.
# Feel free to add or delete extensions to any list, but don't add any new
# compilers unless you write the interface for it yourself.
#
# 'rest' is reStructuredText
# 'markdown' is MarkDown
# 'html' assumes the file is html and just copies it
COMPILERS = {
    "rest": ('.txt', '.rst'),
    "markdown": ('.md', '.mdown', '.markdown'),
    "textile": ('.textile',),
    "txt2tags": ('.t2t',),
    "bbcode": ('.bb',),
    "wiki": ('.wiki',),
    "ipynb": ('.ipynb',),
    "html": ('.html', '.htm')
}

# Create by default posts in one file format?
# Set to False for two-file posts, with separate metadata.
# ONE_FILE_POSTS = True

# If this is set to True, then posts that are not translated to a language
# LANG will not be visible at all in the pages in that language.
# If set to False, the DEFAULT_LANG version will be displayed for
# untranslated posts.
# SHOW_UNTRANSLATED_POSTS = False

# Nikola supports logo display.  If you have one, you can put the URL here.
# Final output is <img src="LOGO_URL" id="logo" alt="BLOG_TITLE">.
# The URL may be relative to the site root.
LOGO_URL = '/logo.png'

# Paths for different autogenerated bits. These are combined with the
# translation paths.

# Final locations are:
# output / TRANSLATION[lang] / TAG_PATH / index.html (list of tags)
# output / TRANSLATION[lang] / TAG_PATH / tag.html (list of posts for a tag)
# output / TRANSLATION[lang] / TAG_PATH / tag.xml (RSS feed for a tag)
# TAG_PATH = "categories"

# If TAG_PAGES_ARE_INDEXES is set to True, each tag's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# TAG_PAGES_ARE_INDEXES = True

# Final location is output / TRANSLATION[lang] / INDEX_PATH / index-*.html
# INDEX_PATH = ""

# Create per-month archives instead of per-year
# CREATE_MONTHLY_ARCHIVE = True
# Final locations for the archives are:
# output / TRANSLATION[lang] / ARCHIVE_PATH / ARCHIVE_FILENAME
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / index.html
# ARCHIVE_PATH = ""
# ARCHIVE_FILENAME = "archive.html"

# Final locations are:
# output / TRANSLATION[lang] / RSS_PATH / rss.xml
# RSS_PATH = ""

# Number of posts in RSS feeds
# FEED_LENGTH = 10

# Slug the Tag URL easier for users to type, special characters are
# often removed or replaced as well.
SLUG_TAG_PATH = True

# A list of redirection tuples, [("foo/from.html", "/bar/to.html")].
#
# A HTML file will be created in output/foo/from.html that redirects
# to the "/bar/to.html" URL. notice that the "from" side MUST be a
# relative URL.
#
# If you don't need any of these, just set to []
# REDIRECTIONS = []

# Commands to execute to deploy. Can be anything, for example,
# you may use rsync:
# "rsync -rav output/* joe@my.site:/srv/www/site"
# And then do a backup, or ping pingomatic.
# To do manual deployment, set it to []
# DEPLOY_COMMANDS = []
from local_conf import DEPLOY_COMMANDS

# Where the output site should be located
# If you don't use an absolute path, it will be considered as relative
# to the location of conf.py
# OUTPUT_FOLDER = 'output'

# where the "cache" of partial generated content should be located
# default: 'cache'
# CACHE_FOLDER = 'cache'

# Filters to apply to the output.
# A directory where the keys are either: a file extensions, or
# a tuple of file extensions.
#
# And the value is a list of commands to be applied in order.
#
# Each command must be either:
#
# A string containing a '%s' which will
# be replaced with a filename. The command *must* produce output
# in place.
#
# Or:
#
# A python callable, which will be called with the filename as
# argument.
#
# By default, there are no filters.

def convert_images(filename):
    EXCLUDE_IMAGES = (
        'assets',
    )
    for exclude in EXCLUDE_IMAGES:
        if exclude in filename:
            continue

    name, ext = os.path.splitext(filename)
    to_filename = name + '.thumbnail' + ext
    command = 'convert {from_filename} -thumbnail 580 {to_filename}'\
            .format(from_filename=filename,
                    to_filename=to_filename)
    os.system(command)

FILTERS = {
    # ".jpg": ["jpegoptim --strip-all -m75 -v %s"],
    ".jpg": [convert_images],
    ".jpeg": [convert_images],
    ".png": [convert_images],
}

# Create a gzipped copy of each generated file. Cheap server-side optimization.
# GZIP_FILES = False
# File extensions that will be compressed
# GZIP_EXTENSIONS = ('.txt', '.htm', '.html', '.css', '.js', '.json')

# #############################################################################
# Image Gallery Options
# #############################################################################

# Galleries are folders in galleries/
# Final location of galleries will be output / GALLERY_PATH / gallery_name
GALLERY_PATH = "galleries"
THUMBNAIL_SIZE = 180
MAX_IMAGE_SIZE = 1280
USE_FILENAME_AS_TITLE = False
GALLERY_SORT_BY_DATE = True
EXTRA_IMAGE_EXTENSIONS = []

# #############################################################################
# HTML fragments and diverse things that are used by the templates
# #############################################################################

# Data about post-per-page indexes
# INDEXES_TITLE = ""  # If this is empty, the default is BLOG_TITLE
# INDEXES_PAGES = ""  # If this is empty, the default is 'old posts page %d'
# translated

# Name of the theme to use.
# THEME = 'site'
THEME = 'elblogdehumitos'

# Color scheme to be used for code blocks. If your theme provides
# "assets/css/code.css" this is ignored.
# Can be any of autumn borland bw colorful default emacs friendly fruity manni
# monokai murphy native pastie perldoc rrt tango trac vim vs
# CODE_COLOR_SCHEME = default

# If you use 'site-reveal' theme you can select several subthemes
# THEME_REVEAL_CONGIF_SUBTHEME = 'sky'
# You can also use: beige/serif/simple/night/default

# Again, if you use 'site-reveal' theme you can select several transitions
# between the slides
# THEME_REVEAL_CONGIF_TRANSITION = 'cube'
# You can also use: page/concave/linear/none/default

# date format used to display post dates.
# (str used by datetime.datetime.strftime)
DATE_FORMAT = '%d-%m-%Y %H:%M'

# FAVICONS contains (name, file, size) tuples.
# Used for create favicon link like this:
# <link rel="name" href="file" sizes="size"/>
# For creating favicons, take a look at:
# http://www.netmagazine.com/features/create-perfect-favicon
FAVICONS = {
    ("icon", "/favicon.ico", "16x16"),
    ("icon", "/favicon_128x128.png", "128x128"),
}

INDEX_TEASERS = True
# 'Read more...' for the index page, if INDEX_TEASERS is True (translatable)
INDEX_READ_MORE_LINK = True
# 'Read more...' for the RSS_FEED, if RSS_TEASERS is True (translatable)
RSS_READ_MORE_LINK = False
RSS_TEASERS = False

# A HTML fragment describing the license, for the sidebar. Default is "".
# I recommend using the Creative Commons' wizard:
# http://creativecommons.org/choose/
LICENSE = """
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">
  <img alt="Licencia Creative Commons" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/4.0/88x31.png" />
</a>"""



# A small copyright notice for the page footer (in HTML).
# (translatable)
CONTENT_FOOTER = '&copy; 2007-{date} <a href="mailto:{email}">{author}</a> - Powered by <a href="http://getnikola.com">Nikola</a>' + \
    '<br/>El contenido de este blog está bajo la licencia Creative Commons,' + \
    '<br/>la misma está disponible completa <a target="_blank" href="http://creativecommons.org/licenses/by-sa/4.0/">aquí.</a>' + \
    '<br/>{license}'

# Things that will be passed to CONTENT_FOOTER.format().  This is done
# for translatability, as dicts are not formattable.  Nikola will
# intelligently format the setting properly.
# The setting takes a dict. The keys are languages. The values are
# tuples of tuples of positional arguments and dicts of keyword arguments
# to format().  For example, {'en': (('Hello'), {'target': 'World'})}
# results in CONTENT_FOOTER['en'].format('Hello', target='World').
# WARNING: If you do not use multiple languages with CONTENT_FOOTER, this
#          still needs to be a dict of this format.  (it can be empty if you
#          do not need formatting)
# (translatable)
CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            "email": BLOG_EMAIL,
            "author": BLOG_AUTHOR,
            "date": time.gmtime().tm_year,
            "license": LICENSE
        }
    )
}

# To use comments, you can choose between different third party comment
# systems, one of "disqus", "livefyre", "intensedebate", "moot",
# "googleplus" or "facebook"
COMMENT_SYSTEM = "disqus"
# And you also need to add your COMMENT_SYSTEM_ID which
# depends on what comment system you use. The default is
# "nikolademo" which is a test account for Disqus. More information
# is in the manual.
COMMENT_SYSTEM_ID = "humitos"

# Create index.html for story folders?
# STORY_INDEX = False
# Enable comments on story pages?
COMMENTS_IN_STORIES = True
# Enable comments on picture gallery pages?
# COMMENTS_IN_GALLERIES = False

# What file should be used for directory indexes?
# Defaults to index.html
# Common other alternatives: default.html for IIS, index.php
INDEX_FILE = "index.html"

# If a link ends in /index.html,  drop the index.html part.
# http://mysite/foo/bar/index.html => http://mysite/foo/bar/
# (Uses the INDEX_FILE setting, so if that is, say, default.html,
# it will instead /foo/default.html => /foo)
# (Note: This was briefly STRIP_INDEX_HTML in v 5.4.3 and 5.4.4)
# Default = False
STRIP_INDEXES = True

# Should the sitemap list directories which only include other directories
# and no files.
# Default to True
# If this is False
# e.g. /2012 includes only /01, /02, /03, /04, ...: don't add it to the sitemap
# if /2012 includes any files (including index.html)... add it to the sitemap
# SITEMAP_INCLUDE_FILELESS_DIRS = True

# List of files relative to the server root (!) that will be asked to be excluded
# from indexing and other robotic spidering. * is supported. Will only be effective
# if SITE_URL points to server root. The list is used to exclude resources from
# /robots.txt and /sitemap.xml, and to inform search engines about /sitemapindex.xml.
ROBOTS_EXCLUSIONS = ["/archive.html", "/category/*.html"]

# Instead of putting files in <slug>.html, put them in
# <slug>/index.html. Also enables STRIP_INDEXES
# This can be disabled on a per-page/post basis by adding
#    .. pretty_url: False
# to the metadata
PRETTY_URLS = True

# Do you want a add a Mathjax config file?
# MATHJAX_CONFIG = ""

# If you are using the compile-ipynb plugin, just add this one:
#MATHJAX_CONFIG = """
#<script type="text/x-mathjax-config">
#MathJax.Hub.Config({
#    tex2jax: {
#        inlineMath: [ ['$','$'], ["\\\(","\\\)"] ],
#        displayMath: [ ['$$','$$'], ["\\\[","\\\]"] ]
#    },
#    displayAlign: 'left', // Change this to 'center' to center equations.
#    "HTML-CSS": {
#        styles: {'.MathJax_Display': {"margin": 0}}
#    }
#});
#</script>
#"""

# What MarkDown extensions to enable?
# You will also get gist, nikola and podcast because those are
# done in the code, hope you don't mind ;-)
# MARKDOWN_EXTENSIONS = ['fenced_code', 'codehilite']

# Social buttons. This is sample code for AddThis (which was the default for a
# long time). Insert anything you want here, or even make it empty.
SOCIAL_BUTTONS_CODE = ""

# Show link to source for the posts?
SHOW_SOURCELINK = True

# Modify the number of Post per Index Page
# Defaults to 10
INDEX_DISPLAY_POST_COUNT = 4

# By default, Nikola generates RSS files for the website and for tags, and
# links to it.  Set this to False to disable everything RSS-related.
GENERATE_RSS = True

# RSS_LINK is a HTML fragment to link the RSS or Atom feeds. If set to None,
# the base.tmpl will use the feed Nikola generates. However, you may want to
# change it for a feedburner feed or something else.
# RSS_LINK = None

# Show only teasers in the RSS feed? Default to True
# RSS_TEASERS = True

# Strip HTML in the RSS feed? Default to False
# RSS_PLAIN = False

# A search form to search this site, for the sidebar. You can use a google
# custom search (http://www.google.com/cse/)
# Or a duckduckgo search: https://duckduckgo.com/search_box.html
# Default is no search form.
# SEARCH_FORM = ""
#
# This search form works for any site and looks good in the "site" theme where
# it appears on the navigation bar:
#
#SEARCH_FORM = """
#<!-- Custom search -->
#<form method="get" id="search" action="http://duckduckgo.com/"
# class="navbar-form pull-left">
#<input type="hidden" name="sites" value="%s"/>
#<input type="hidden" name="k8" value="#444444"/>
#<input type="hidden" name="k9" value="#D51920"/>
#<input type="hidden" name="kt" value="h"/>
#<input type="text" name="q" maxlength="255"
# placeholder="Search&hellip;" class="span2" style="margin-top: 4px;"/>
#<input type="submit" value="DuckDuckGo Search" style="visibility: hidden;" />
#</form>
#<!-- End of custom search -->
#""" % SITE_URL
#
# If you prefer a google search form, here's an example that should just work:
#SEARCH_FORM = """
#<!-- Custom search with google-->
#<form id="search" action="http://google.com/search" method="get" class="navbar-form pull-left">
#<input type="hidden" name="q" value="site:%s" />
#<input type="text" name="q" maxlength="255" results="0" placeholder="Search"/>
#</form>
#<!-- End of custom search -->
#""" % SITE_URL

# Also, there is a local search plugin you can use, based on Tipue, but it requires setting several
# options:

# SEARCH_FORM = """
# <span class="navbar-form pull-left">
# <input type="text" id="tipue_search_input">
# </span>"""
#
# ANALYTICS = """
# <script type="text/javascript" src="/assets/js/tipuesearch_set.js"></script>
# <script type="text/javascript" src="/assets/js/tipuesearch.js"></script>
# <script type="text/javascript">
# $(document).ready(function() {
    # $('#tipue_search_input').tipuesearch({
        # 'mode': 'json',
        # 'contentLocation': '/assets/js/tipuesearch_content.json',
        # 'showUrl': false
    # });
# });
# </script>
# """

EXTRA_HEAD_DATA = """
<meta name="twitter:card" content="summary">
<meta name="twitter:site" content="@reydelhumo">
<meta name="twitter:title" content="Novedades">
<meta name="twitter:description" content="Novedades sobre &quot;Argentina en Python&quot;">
<meta name="twitter:creator" content="@argenpython">
<meta name="twitter:image:src" content="http://elblogdehumitos.com.ar/pages/argentina-en-python/logo.png">
<meta name="twitter:domain" content="elblogdehumitos.com.ar">
<meta name="twitter:app:name:iphone" content="">
<meta name="twitter:app:name:ipad" content="">
<meta name="twitter:app:name:googleplay" content="">
<meta name="twitter:app:url:iphone" content="">
<meta name="twitter:app:url:ipad" content="">
<meta name="twitter:app:url:googleplay" content="">
<meta name="twitter:app:id:iphone" content="">
<meta name="twitter:app:id:ipad" content="">
<meta name="twitter:app:id:googleplay" content="">
"""

# Use content distribution networks for jquery and twitter-bootstrap css and js
# If this is True, jquery is served from the Google CDN and twitter-bootstrap
# is served from the NetDNA CDN
# Set this to False if you want to host your site without requiring access to
# external resources.
# USE_CDN = False

# Extra things you want in the pages HEAD tag. This will be added right
# before </HEAD>
# EXTRA_HEAD_DATA = ""
# Google analytics or whatever else you use. Added to the bottom of <body>
# in the default template (base.tmpl).
BODY_END = """
<script src="/assets/js/jquery.timeago.js" type="text/javascript"></script>
<script>
    jQuery(document).ready(function() {

	if(jQuery('html').attr('lang') === 'es'){
	    jQuery.timeago.settings.strings = {
		prefixAgo: "hace",
		prefixFromNow: "dentro de",
		suffixAgo: "",
		suffixFromNow: "",
		seconds: "menos de un minuto",
		minute: "un minuto",
		minutes: "unos %d minutos",
		hour: "una hora",
		hours: "%d horas",
		day: "un día",
		days: "%d días",
		month: "un mes",
		months: "%d meses",
		year: "un año",
		years: "%d años"
	    };
	}
	jQuery("time.published").timeago();

	jQuery('article:not(:first)').before('<hr>');

	jQuery('.highlight pre').addClass('code');
    });
</script>


<script src="http://cdn.leafletjs.com/leaflet-0.7.3/leaflet.js"></script>
<link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.7.3/leaflet.css" />

<script type="text/javascript">
  $.getJSON("/assets/js/point.json", function(data){
      var map = L.map('map').setView(data, 11);

      // create the tile layer with correct attribution
      var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
      var osmAttrib='Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
      var osm = new L.TileLayer(osmUrl, {minZoom: 8, maxZoom: 14, attribution: osmAttrib});
      map.addLayer(osm);

      var marker = L.marker(data).addTo(map);
      marker.bindPopup("<b>Humitos</b> está aquí!").openPopup();
  });
</script>

<a title="Real Time Web Analytics" href="http://clicky.com/100758465">
  <img alt="Real Time Web Analytics" src="//static.getclicky.com/media/links/badge.gif" border="0" />
</a>
<script src="//static.getclicky.com/js" type="text/javascript"></script>
<script type="text/javascript">try{ clicky.init(100758465); }catch(e){}</script>
<noscript><p><img alt="Clicky" width="1" height="1" src="//in.getclicky.com/100758465ns.gif" /></p></noscript>

<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
"""

# The possibility to extract metadata from the filename by using a
# regular expression.
# To make it work you need to name parts of your regular expression.
# The following names will be used to extract metadata:
# - title
# - slug
# - date
# - tags
# - link
# - description
#
# An example re is the following:
# '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)-(?P<title>.*)\.md'
# FILE_METADATA_REGEXP = None

# If you hate "Filenames with Capital Letters and Spaces.md", you should
# set this to true.
UNSLUGIFY_TITLES = True

# Nikola supports Twitter Card summaries / Open Graph.
# Twitter cards make it possible for you to attach media to Tweets
# that link to your content.
#
# IMPORTANT:
# Please note, that you need to opt-in for using Twitter Cards!
# To do this please visit
# https://dev.twitter.com/form/participate-twitter-cards
#
# Uncomment and modify to following lines to match your accounts.
# Specifying the id for either 'site' or 'creator' will be preferred
# over the cleartext username. Specifying an ID is not necessary.
# Displaying images is currently not supported.
# TWITTER_CARD = {
#     # 'use_twitter_cards': True,  # enable Twitter Cards / Open Graph
#     # 'site': '@website',  # twitter nick for the website
#     # 'site:id': 123456,  # Same as site, but the website's Twitter user ID
#                           # instead.
#     # 'creator': '@username',  # Username for the content creator / author.
#     # 'creator:id': 654321,  # Same as creator, but the Twitter user's ID.
# }


# Post's dates are considered in UTC by default, if you want to use
# another time zone, please set TIMEZONE to match. Check the available
# list from Wikipedia:
# http://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# (eg. 'Europe/Zurich')
# Also, if you want to use a different time zone in some of your posts,
# you can use the ISO 8601/RFC 3339 format (ex. 2012-03-30T23:00:00+02:00)
TIMEZONE = 'America/Argentina/Buenos_Aires'

# If webassets is installed, bundle JS and CSS to make site loading faster
# USE_BUNDLES = True

# Plugins you don't want to use. Be careful :-)
# DISABLED_PLUGINS = ["render_galleries"]

# List of regular expressions, links matching them will always be considered
# valid by "nikola check -l"
# LINK_CHECK_WHITELIST = []

# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.

GLOBAL_CONTEXT = {}
