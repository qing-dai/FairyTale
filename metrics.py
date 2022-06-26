from text_exp import find_pos

from typing import List, Tuple, Counter
import spacy

nlp = spacy.load('en_core_web_sm')


def find_pos_in_three_parts(split_file: Tuple[List[str], List[str], List[str]], pos: str) -> List[Counter]:
    """Find pos in first, middle and end of a file

    :param split_file:The tuple containing three even length lists of strings, converted from a fairy tale.
    :param pos: The POS to be checked.
    :return: The list containing three counters with token_lemmas with their count, corresponding beginning, middle and end part of
    a file.
    """
    pos_list = []
    for lines in split_file:
        pos_dict = find_pos(lines, pos)
        pos_list.append(pos_dict)
    return pos_list



