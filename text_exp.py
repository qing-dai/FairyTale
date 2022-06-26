from typing import TextIO, List, Tuple
from collections import Counter

import spacy

nlp = spacy.load('en_core_web_sm')


def split_text(file: TextIO) -> Tuple[List[str], List[str], List[str]]:
    """
    Split a text into three even-length parts.

    :param file: The fairy tale file to be split.
    :return: The tuple containing three even-length lists of strings.
    """
    lines = file.readlines()
    file_len = len(lines)
    first_part = lines[:int(file_len / 3)]
    middle_part = lines[int(file_len / 3): int(2 * (file_len / 3))]
    end_part = lines[int(2 * (file_len / 3)):]
    return first_part, middle_part, end_part


def find_pos(str_list: List[str], pos: str) -> Counter:
    """Find frequency of a certain POS

    :param str_list: The list of strings.
    :param pos: The POS to be located in the list.
    :return: The counter of POS to be checked, the token's lemma with its count.
    """
    pos_counter = Counter()
    for strs in str_list:
        for token in nlp(strs.lower()):
            # We are excluding stop words since we're only focusing on content words.
            if token.pos_ == pos and not token.is_stop:
                pos_counter[token.lemma_] += 1
    return pos_counter




