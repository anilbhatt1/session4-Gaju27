import inspect
import os
import re

import pytest

import session4

README_CONTENT_CHECK_FOR = [
    'and',
    'or',
    'repr',
    'str',
    'add',
    'eq',
    'float',
    'ge',
    'gt',
    'invertsign',
    'le',
    'lt',
    'mul',
    'sqrt',
    'bool'
]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 1, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_invalid_real_Exception_provides_relevant_message():
    with pytest.raises(Exception, match=r".* real .*"):
        session4.Qualean(2)

def test_addition():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(-1)
    q3 = q1 + q2
    assert q3 == q1.__add__(q2)

def test_in_equality():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(0)
    assert q1.__ne__(q2)


def test_class_repr():
    s = session4.Qualean(1)
    s_n = session4.Qualean(0)
    assert 'object at' not in s.__repr__() and 'object at' not in s_n.__repr__()


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_less_than_equal():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(-1)
    assert q1.__le__(q2)


def test_less_than():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(0)
    assert q1.__lt__(q2)


def test_and_assertion():
    q1, q2, q3 = session4.Qualean(-1), session4.Qualean(1), session4.Qualean(0)

    assert bool(q1) and bool(q2) == True
    assert bool(q1) and bool(q3) == False
    assert bool(q2) and bool(q3) == False


def test_or_assertion():
    q1, q2, q3 = session4.Qualean(-1), session4.Qualean(1), session4.Qualean(0)

    assert bool(q1) or bool(q2) == True
    assert bool(q1) or bool(q3) == True
    assert bool(q2) or bool(q3) == True
    assert bool(q3) or bool(q3) == False