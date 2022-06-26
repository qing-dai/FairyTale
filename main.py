"""
Extract content words based on a certain POS choice from a fairy tale.
"""

from argparse import ArgumentParser, FileType

from collections import Counter

from metrics import find_pos_in_three_parts
from text_exp import split_text


def format_metric(name: str, pos_list: list) -> str:
    """Format results for console output."""
    message = f"\n{name}"
    n = 0
    file_structure = ["Beginning", "Middle", "End"]
    for ps_counter in pos_list:
        pos_dict = dict(ps_counter.most_common())
        message += f"\n\n{file_structure[n]}:\t\t{pos_dict}"
        n += 1
    return message


def get_argument_parser() -> ArgumentParser:
    parser = ArgumentParser(description="Extract content words based on a certain POS choice from a fairy tale.")
    parser.add_argument('tale1', type=FileType('r', encoding='utf-8'),
                        help="A fairy tale text.")
    parser.add_argument('--tale2', type=FileType('r', encoding='utf-8'),
                        help="Another fairy tale text if you want to compare.")
    parser.add_argument('pos', type=str,
                        help="Please choose a pos from 'NOUN','VERB','ADJ' or 'ADV'.")
    parser.add_argument("--number1", '-n1', type=int,
                        help="Please enter a number for the N most frequent POS you want to display within this tale.")
    parser.add_argument("--number2", '-n2', type=int, default=10,
                        help="Please enter a number for the N most frequently shared POS between the two tales, default is 10." )
    return parser


def main():

    # Parse command line arguments
    parser = get_argument_parser()
    args = parser.parse_args()
    # Split a tale into three parts with even line length.
    three_even_part = split_text(args.tale1)
    # Get the POS frequency respectively in the beginning, middle and end.
    pos_list = find_pos_in_three_parts(three_even_part, args.pos)
    print(format_metric(f"The {args.pos} in the beginning, the middle and the end of this fairy tale is:", pos_list))
    # Get the n most frequent pos in a tale
    total_pos = pos_list[0] + pos_list[1] + pos_list[2]
    if args.number1:
        if args.number1 <= len(total_pos):
            top_pos = total_pos.most_common(args.number1)
            print(f"\n\n-------------------------cutting--line-----------------------")
            print(f"\nThe {args.number1} most frequent {args.pos} in this fairy tale is:\n")
            for word, count in top_pos:
                print(f"{count}\t\t{word}")
        else:
            print(f"\n\nYour number1 exceeds the count under this type which is '{len(total_pos)}', please try a new number less or equal.")
    # Get the pos list for tale2 and compare the common pos between these two fairy tales.
    if args.tale2:
        three_even_part2 = split_text(args.tale2)
        pos_list2 = find_pos_in_three_parts(three_even_part2, args.pos)
        total_pos2 = pos_list2[0] + pos_list2[1] + pos_list2[2]
        common_pos_dict = {x: (total_pos[x], total_pos2[x]) for x in total_pos if x in total_pos2}
        if args.number2 <= len(common_pos_dict):
            top_common_pos = Counter(common_pos_dict).most_common(args.number2)
            print(f"\n\n-------------------------cutting--line-----------------------")
            print(f"\nThe {args.number2} most common {args.pos} between these two fairy tales are:\n")
            for word, count in top_common_pos:
                print(f"{count[0]} , {count[1]}\t\t{word}")
        else:
            print(f"\n\nYour number2 exceeds the shared count '{len(common_pos_dict)}', please enter a new number less or equal.")


if __name__ == '__main__':
    main()
