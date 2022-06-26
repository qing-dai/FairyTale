import pytest

from collections import Counter

from metrics import find_pos_in_three_parts


@pytest.fixture
def split_three_tuple():
    return (
        ['They themselves knew not how old they were, but they could remember\n',
         'very well that there had been many more; that they were of a family\n'],
        ['from foreign lands, and that for them and theirs the whole forest was\n',
         'planted.They had never been outside it, but they knew that there was\n'],
        ['still something more in the world, which was called the manor-house, and\n',
         'that there they were boiled, and then they became black.\n']
    )


def test_find_noun_in_three_parts(split_three_tuple):
    assert find_pos_in_three_parts(split_three_tuple, pos="NOUN") == [Counter({'family': 1}),
                                                                      Counter({'land': 1, 'forest': 1}),
                                                                      Counter({'world': 1, 'manor': 1, 'house': 1})]

