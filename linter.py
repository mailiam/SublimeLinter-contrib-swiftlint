#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by SeJun Jeong
# Copyright (c) 2016 SeJun Jeong
#
# License: MIT
#

"""This module exports the Swiftlint plugin class."""

from SublimeLinter.lint import Linter, util


class Swiftlint(Linter):
    """Provides an interface to swiftlint."""

    syntax = 'swift'
    cmd = ('swiftlint', 'lint', '--use-stdin')
    executable = None
    version_args = 'version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.9.1'
    regex = (
        r'^.+?:(?P<line>\d+):(?P<col>\d+)?:? '
        r'(?:(?P<error>error)|(?P<warning>warning)): '
        r'(?P<message>.+)'
    )
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None

