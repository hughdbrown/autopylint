"""
Regexes used for the editor's table
"""
import re


MODULE_NAME = re.compile(r"""
    ^\*+\s
    Module\s+
    (?P<filename>[\w\d\._-]+)
    $
""", re.VERBOSE)

#C: 75, 0: Unnecessary parens after 'print' keyword (superfluous-parens)
#C: 14, 0: Too many lines in module (6953/1000) (too-many-lines)
PYLINT_ITEM = re.compile(r"""
    ^
    (?P<type>[ERCW]):
    \s*
    (?P<where1>\d+),
    \s*
    (?P<where2>-?\d+):
    \s+
    (?P<desc>[\w\d\s\.\(\)/',]+?)
    \s
    \(
    (?P<error>[\w_\.-]+?)
    \)
    $
""", re.VERBOSE)


# Some pylint errors do not have the error type until the second line after.
PYLINT_SEMI_ITEM = re.compile(r"""
    ^
    (?P<type>[ERCW]):
    \s*
    (?P<where1>\d+),
    \s*
    (?P<where2>-?\d+):
    \s+
    (?P<desc>[\w\d\s\.\(\)/]+?)
    $
""", re.VERBOSE)


PYLINT_ERROR_ITEM = re.compile(r"""
    ^
    [\^\s\|]+
    \(
    (?P<error>[\w_\.-]+)
    \)
    $
""", re.VERBOSE)
