"""
Regexes used for pylint rules
"""
import re


STD_IMPORT = re.compile(r"""
    ^
    standard\simport\s
    \"(?P<before>[^"]+)\"
    \sshould\sbe\splaced\sbefore\s
    \"(?P<after>[^"]+)\"
    $
""", re.VERBOSE)

FROM_IMP = re.compile(r"""
    ^
    from
    \s+(?P<library>[\w\d_\.]+)
    \s+import
    \s+(?P<imports>[\w\d_\.,\s]+)
    $
""", re.VERBOSE)

IF_STMT_AND = re.compile(r"""
    ^
    if\s+
    (?P<first>.*?)
    \s+and\s+
    (?P<second>.*?):
    $
""", re.VERBOSE)


IF_STMT_OR = re.compile(r"""
    ^
    if\s+
    (?P<first>.*?)
    \s+or\s+
    (?P<second>.*?):
    $
""", re.VERBOSE)


CONTINUATION = re.compile(r"""
    ^
    Wrong\scontinued\sindentation\s
    \(
    (?P<verb>.*?)
    \s(?P<count>\d+)\s+spaces
    \)
    \.
    $
""", re.VERBOSE)


HANGING = re.compile(r"""
    ^
    Wrong\shanging\sindentation\s
    (
        \(
        (?P<verb>.*?)
        \s(?P<count>\d+)\s+spaces
        \)
    )?
    \.
    $
""", re.VERBOSE)
