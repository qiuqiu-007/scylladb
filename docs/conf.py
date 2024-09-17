# -*- coding: utf-8 -*-
import os
import sys
import warnings
from datetime import date

from sphinx_scylladb_theme.utils import multiversion_regex_builder
from recommonmark.transform import AutoStructify

sys.path.insert(0, os.path.abspath('./_ext'))
sys.path.insert(0, os.path.abspath(".."))

# -- Global variables

# Set the base URL for the documentation site.
BASE_URL = 'https://opensource.docs.scylladb.com'
# Build documentation for the following tags and branches.
TAGS = []
BRANCHES = ["master", "branch-5.1", "branch-5.2", "branch-5.4", "branch-6.0", "branch-6.1", "branch-6.2"]
# Set the latest version. 
LATEST_VERSION = "branch-6.1"
# Set which versions are not released yet.
UNSTABLE_VERSIONS = ["master", "branch-6.2"]
# Set which versions are deprecated.
DEPRECATED_VERSIONS = [""]

# -- General configuration

# Add any Sphinx extension module names here, as strings.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.githubpages",
    "sphinx.ext.extlinks",
    "sphinx_sitemap",
    "sphinx_scylladb_theme",
    "sphinx_multiversion",
    "sphinx_scylladb_markdown",
    "sphinxcontrib.datatemplates",
    "scylladb_cc_properties",
    "scylladb_aws_images",
    "scylladb_azure_images",
    "scylladb_gcp_images",
    "scylladb_include_flag",
    "scylladb_dynamic_substitutions",
    "scylladb_swagger",
    "scylladb_metrics"
]

# The suffix(es) of source filenames.
source_suffix = ['.rst']

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "ScyllaDB Open Source"
copyright = str(date.today().year) + ", ScyllaDB. All rights reserved."
author = u"ScyllaDB Project Contributors"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'lib', 'lib64','**/_common/*', 'README.md', 'index.md', '.git', '.github', '_utils', 'rst_include', 'venv', 'dev', '_data/**']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# List of substitutions
rst_prolog = """
.. |mon_root| replace::  `Scylla Monitoring Stack <https://monitoring.docs.scylladb.com>`__
.. |cql-version| replace:: 3.3.1
"""

# -- Options for not found extension

# Template used to render the 404.html generated by this extension.
notfound_template = "404.html"

# Prefix added to all the URLs generated in the 404 page.
notfound_urls_prefix = ""

# -- Options for markdown extension
scylladb_markdown_enable = True
scylladb_markdown_recommonmark_versions = ['branch-5.1', 'branch-5.2', 'branch-5.4']
suppress_warnings = ["myst.xref_missing"]

# -- Options for sitemap extension

sitemap_url_scheme = "/stable/{link}"

# -- Options for multiversion extension

# Whitelist pattern for tags
smv_tag_whitelist = multiversion_regex_builder(TAGS)
# Whitelist pattern for branches
smv_branch_whitelist = multiversion_regex_builder(BRANCHES)
# Defines which version is considered to be the latest stable version.
smv_latest_version = LATEST_VERSION
# Defines the new name for the latest version.
smv_rename_latest_version = "stable"
# Whitelist pattern for remotes (set to None to use local branches only)
smv_remote_whitelist = r"^origin$"
# Pattern for released versions
smv_released_pattern = r"^tags/.*$"
# Format for versioned output directories inside the build directory
smv_outputdir_format = "{ref.name}"

# -- Options for scylladb_aws_images extension

scylladb_aws_images_base_url = "https://s3.amazonaws.com/downloads.scylladb.com"
scylladb_aws_images_ami_bucket_directory = "downloads/scylla/aws/ami/"
scylladb_aws_images_ami_download_directory = "_data/opensource/aws/ami"
scylladb_aws_images_cloudformation_bucket_directory = "downloads/scylla/aws/cloudformation/"

# -- Options for scylladb_azure_images extension
scylladb_azure_images_base_url = "https://s3.amazonaws.com/downloads.scylladb.com"
scylladb_azure_images_bucket_directory = "downloads/scylla/azure/"
scylladb_azure_images_download_directory = "_data/opensource/azure"

# -- Options for scylladb_gcp_images extension
scylladb_gcp_images_base_url = "https://s3.amazonaws.com/downloads.scylladb.com"
scylladb_gcp_images_bucket_directory = "downloads/scylla/gce/"
scylladb_gcp_images_download_directory = "_data/opensource/gce"

# -- Options for scylladb_swagger extension
scylladb_swagger_origin_api = "../api"
scylladb_swagger_template = "swagger.tmpl"
scylladb_swagger_inc_template = "swagger_inc.tmpl"

# -- Options for scylladb_metrics
scylladb_metrics_directory = "_data/opensource/metrics"


# -- Options for HTML output

# The theme to use for pages.
html_theme = "sphinx_scylladb_theme"
templates_path = ['_templates', ]

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for the theme, see the
# documentation.
html_theme_options = {
    "conf_py_path": "docs/",
    'hide_banner': 'true',
    "hide_edit_this_page_button": "false",
    "hide_feedback_buttons": 'false',
    "github_issues_repository": "scylladb/scylladb",
    "github_repository": "scylladb/scylladb",
    "github_label": "type/documentation",
    "versions_unstable": UNSTABLE_VERSIONS,
    "versions_deprecated": DEPRECATED_VERSIONS,
    'banner_button_text': 'Register for Free',
    'banner_button_url': 'https://lp.scylladb.com/university-live-2023-03-registration?siteplacement=docs',
    'banner_title_text': 'ScyllaDB University LIVE, FREE Virtual Training Event | March 21',
    "collapse_navigation": 'true',
}

# Last updated format
html_last_updated_fmt = "%d %b %Y"

# Custom sidebar templates, maps document names to template names.
html_sidebars = {"**": ["side-nav.html"]}

# Output file base name for HTML help builder.
htmlhelp_basename = "ScyllaDocumentationdoc"

# URL which points to the root of the HTML documentation.
html_baseurl = BASE_URL

# Dictionary of values to pass into the template engine’s context for all pages
html_context = {"html_baseurl": html_baseurl}

def setup(app):
    if 'opensource' in app.tags:
        app.tags.add('experimental')
