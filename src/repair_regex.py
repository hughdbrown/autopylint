"""
Module of repairs to do to source code.
"""

COMPARISONS = r"(>=|<=|>|<|!=|==)"
ASSIGNMENTS = r"(\+=|-=|/=|\*=|=)"
START_BRACKETS = r"(\{|\[|\()"
END_BRACKETS = r"(\}|\]|\))"

WHITESPACE_TABLE = {
    "Exactly one space required after :": [
        (r":\s*(\S+)", r": \1", {}),
        # (r":\s+", ": "),
        # (r":(\S+)", r": \1"),
    ],
    "Exactly one space required after comma": [
        (r"(.*?),\s*", r"\1, ", {}),
    ],
    "Exactly one space required after comparison": [
        (r"(.*?){0}\s*(\S+)".format(COMPARISONS), r"\1\2 \3", {}),
        # (r"(.*){0}\s+".format(COMPARISONS), r"\1\2 ", {}),
        # (r"(.*){0}(\S+)".format(COMPARISONS), r"\1\2 \3", {}),
    ],
    "Exactly one space required around assignment": [
        (r"(.*?[\w\d_\[\]\(\)]+)\s*{0}\s*(\S+)".format(ASSIGNMENTS), r"\1 \2 \3", {'count': 1}),
        # (r"(.*\S+)=\s+", r"\1 = ", {'count': 1}),
        # (r"(.*)\s+=(\S+)", r"\1 = \2", {'count': 1}),
        # (r"(.*)\s+=\s+", r"\1 = ", {'count': 1}),
    ],
    "Exactly one space required around comparison": [
        (r"(.*\S+)\s*{0}\s*".format(COMPARISONS), r"\1 \2 ", {}),
        # (r"(.*)\s+{0}\s+".format(COMPARISONS), r"\1 \2", {}),
        # (r"(.*\S+){0}\s+".format(COMPARISONS), r"\1 \2 ", {}),
        # (r"(.*)\s+{0}(\S+)".format(COMPARISONS), r"\1 \2 \3", {}),
        # (r"(.*\S+){0}(\S+)".format(COMPARISONS), r"\1 \2 \3", {}),
    ],
    "No space allowed around keyword argument assignment": [
        (r"(.*\S+)\s*{0}\s*(\S+)".format(ASSIGNMENTS), r"\1\2\3", {'count': 1}),
        # (r"(.*\S+)=\s+", r"\1=", {'count': 1}),
        # (r"(.*)\s+=(\S+)", r"\1=\2", {'count': 1}),
        # (r"(.*\S+)=(\S+)", r"\1=\2", {'count': 1}),
    ],
    "No space allowed before :": [
        (r"(.*?)\s+:", r"\1:", {}),
    ],
    "No space allowed after bracket": [
        (r"(.*?){0}\s+".format(START_BRACKETS), r"\1\2", {}),
    ],
    "No space allowed before bracket": [
        (r"(.*?)\s+{0}".format(END_BRACKETS), r"\1\2", {}),
    ],
    "No space allowed before comma": [
        (r"(.*?)\s+,", r"\1,", {}),
    ],
}
