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

from SublimeLinter.lint import Linter


class Swiftlint(Linter):
    """Provides an interface to swiftlint."""

    cmd = ('swiftlint', 'lint', '--use-stdin', '--quiet')
    regex = (
        r'^.+?:(?P<line>\d+):(?P<col>\d+)?:? '
        r'(?:(?P<error>error)|(?P<warning>warning)): '
        r'(?P<message>.+)'
    )
    defaults = {
        'selector': 'source.swift'
    }
