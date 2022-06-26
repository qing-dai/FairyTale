import pytest

from text_exp import find_pos

from collections import Counter


@pytest.fixture
def string_list():
    return [
        "The flakes of snow covered her long fair hair,\n",
        "which fell in beautiful curls around her neck;\n"
    ]


def test_find_noun_pos(string_list):
    assert find_pos(string_list, pos="NOUN") == Counter(
        {'flake': 1, 'snow': 1, 'hair': 1, 'curl': 1, 'neck': 1})


def test_find_verb_pos(string_list):
    assert find_pos(string_list, pos="VERB") == Counter({'cover': 1, 'fall': 1})


def test_find_adj_pos(string_list):
    assert find_pos(string_list, pos="ADJ") == Counter({'long': 1, 'fair': 1, 'beautiful': 1})
