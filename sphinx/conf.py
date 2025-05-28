# pylint: disable=missing-module-docstring, invalid-name

# -- General configuration ----------------------------------------------------

# Add any Sphinx extension module names here, as strings.
# They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    # let's use MyST markdown
    'myst_parser',
    'sphinx.ext.mathjax',
]

myst_enable_extensions = [
    "dollarmath",
]

# The suffix of source filenames.
source_suffix = '.md'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = "UE22 - Projets d'Informatique"
copyright = "2023, Équipe UE22"           # pylint: disable=redefined-builtin

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.1'
# The full version, including alpha/beta/rc tags.
release = '0.1'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    'conf.py',
    'index-template.md',
]

# The reST default role (used for this markup: `text`)
# to use for all documents.
# default_role = None

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_logo = 'logo-p24.svg'
html_theme = 'sphinx_rtd_theme'
html_theme_options = dict(
    display_version=False,
    prev_next_buttons_location='both',
    style_external_links=True,
    style_nav_header_background='#29a8b9',
)

# inject our own CSS
html_static_path = ['.']
html_css_files = ['custom.css']
