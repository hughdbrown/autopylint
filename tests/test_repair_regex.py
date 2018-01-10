"""
Test module for autopylint
"""
import re

import pytest

from src.python.autopylint.repair_regex import (
    WHITESPACE_TABLE,
    ASSIGNMENTS,
)


class TestAutopylintRegex(object):
    @pytest.mark.parametrize(
        "src,expected",
        [
            ("i = 1", "="),
            ("i += 1", "+="),
            ("i -= 1", "-="),
            ("i /= 1", "/="),
            ("i *= 1", "*="),
        ]
    )
    def test_assignment(self, src, expected):
        m = re.match(r"^.*?" + ASSIGNMENTS, src)
        assert m, src
        assert m.group(1) == expected, src

    @pytest.mark.parametrize(
        "src,expected",
        [
            ("h=None", "h = None"),
            ("h =None", "h = None"),
            ("h= None", "h = None"),
            ("h=  None", "h = None"),
            ("h  =None", "h = None"),
            ("h  =  None", "h = None"),
            (
                "p=[i for i in x if i.type == t]",
                "p = [i for i in x if i.type == t]"
            ),
        ]
    )
    def test_whitespace_assignment(self, src, expected):
        key = "Exactly one space required around assignment"
        regex, repl, kwargs = WHITESPACE_TABLE[key][0]
        result = re.sub(regex, repl, src, **kwargs)
        assert result == expected

    @pytest.mark.parametrize(
        "src,expected",
        [
            ("{'a':1, 'b':  2}", "{'a': 1, 'b': 2}"),
            ("{'a':1, 'b':2}", "{'a': 1, 'b': 2}"),
            ("{'a':  1, 'b':2}", "{'a': 1, 'b': 2}"),
        ]
    )
    def test_whitespace_colon(self, src, expected):
        key = "Exactly one space required after :"
        regex, repl, kwargs = WHITESPACE_TABLE[key][0]
        result = re.sub(regex, repl, src, **kwargs)
        assert result == expected

    @pytest.mark.parametrize(
        "src,expected",
        [
            ("{'a': 1,'b': 2}", "{'a': 1, 'b': 2}"),
            ("{'a': 1,  'b': 2}", "{'a': 1, 'b': 2}"),
        ]
    )
    def test_whitespace_comma(self, src, expected):
        key = "Exactly one space required after comma"
        regex, repl, kwargs = WHITESPACE_TABLE[key][0]
        result = re.sub(regex, repl, src, **kwargs)
        assert result == expected

    @pytest.mark.parametrize(
        "src,expected",
        [
            ("if a >b:", "if a > b:"),
            ("if a >=b:", "if a >= b:"),
            ("if a <b:", "if a < b:"),
            ("if a <=b:", "if a <= b:"),
            ("if a ==b:", "if a == b:"),
            ("if a !=b:", "if a != b:"),
            ("if a >  b:", "if a > b:"),
            ("if a >=  b:", "if a >= b:"),
            ("if a <  b:", "if a < b:"),
            ("if a <=  b:", "if a <= b:"),
            ("if a ==  b:", "if a == b:"),
            ("if a !=  b:", "if a != b:"),
        ]
    )
    def test_whitespace_space_after_comparison(self, src, expected):
        key = "Exactly one space required after comparison"
        regex, repl, kwargs = WHITESPACE_TABLE[key][0]
        result = re.sub(regex, repl, src, **kwargs)
        assert result == expected

    @pytest.mark.parametrize(
        "src,expected",
        [
            ("foo(arg = 3)", "foo(arg=3)"),
            ("foo(arg= 3)", "foo(arg=3)"),
            ("foo(arg =3)", "foo(arg=3)"),
        ]
    )
    def test_whitespace_space_around_keyword(self, src, expected):
        key = "No space allowed around keyword argument assignment"
        regex, repl, kwargs = WHITESPACE_TABLE[key][0]
        result = re.sub(regex, repl, src, **kwargs)
        assert result == expected

    @pytest.mark.parametrize(
        "src,expected",
        [
            ("if a > b :", "if a > b:"),
        ]
    )
    def test_whitespace_space_before_colon(self, src, expected):
        key = "No space allowed before :"
        regex, repl, kwargs = WHITESPACE_TABLE[key][0]
        result = re.sub(regex, repl, src, **kwargs)
        assert result == expected

    @pytest.mark.parametrize(
        "src,expected",
        [
            ("foo( 1, 2)", "foo(1, 2)"),
        ]
    )
    def test_whitespace_space_after_bracket(self, src, expected):
        key = "No space allowed after bracket"
        regex, repl, kwargs = WHITESPACE_TABLE[key][0]
        result = re.sub(regex, repl, src, **kwargs)
        assert result == expected

    @pytest.mark.parametrize(
        "src,expected",
        [
            ("foo(1, 2 )", "foo(1, 2)"),
        ]
    )
    def test_whitespace_space_before_bracket(self, src, expected):
        key = "No space allowed before bracket"
        regex, repl, kwargs = WHITESPACE_TABLE[key][0]
        result = re.sub(regex, repl, src, **kwargs)
        assert result == expected

    @pytest.mark.parametrize(
        "src,expected",
        [
            ("a , b , c", "a, b, c"),
        ]
    )
    def test_whitespace_space_before_comma(self, src, expected):
        key = "No space allowed before comma"
        regex, repl, kwargs = WHITESPACE_TABLE[key][0]
        result = re.sub(regex, repl, src, **kwargs)
        assert result == expected

