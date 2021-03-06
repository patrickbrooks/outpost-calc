#!/usr/local/bin/python
""" Calculate card totals for the Outpost board game """
#
# outpost_calc.py
#
import argparse
from collections import Counter, OrderedDict
from itertools import combinations
import logging
from sys import stdout
from time import perf_counter


# Prepare a logger that prints to stdout
log = logging.getLogger(__name__)
stdout_handler = logging.StreamHandler(stdout)
stdout_handler.setFormatter(logging.Formatter('%(levelname)-8s %(message)s'))
log.addHandler(stdout_handler)

def parse_cmd_line():
    """ Provide command-line help and collection of user-supplied arguments. """
    parser = argparse.ArgumentParser(description="Calculate Outpost card totals")
    parser.add_argument("cards",
                        help='period-separated list of card values (ex. 1.5.7.7.8.13)')
    parser.add_argument("-l", "--loglevel",
                        help='set logging level (default is warn)',
                        choices=['warn', 'info', 'debug'],
                        default='warn')
    args = parser.parse_args()

    # Default log level of warn is set in --loglevel, above
    if args.loglevel == 'debug':
        log.setLevel(logging.DEBUG)
    elif args.loglevel == 'info':
        log.setLevel(logging.INFO)
    elif args.loglevel == 'warn':
        log.setLevel(logging.WARN)
    else:
        log.error("Unexpected log level = {args.loglevel}\nExiting.\n")
        exit(1)

    return {
        'cards_str' : args.cards
    }

def valid_cards_syntax(cards_str):
    """ Confirm that only numeric values separated by periods was given as input """
    cards = cards_str.split('.')
    for c in cards:
        if not c.isnumeric():
            return 'Cards must contain only digits 0-9 separated by periods'
    return None


def find_unique_totals(cards_num):
    """ Brute-force through all possible combinations of cards to find totals. """

    # Return the cards used for each possible total
    #   key = total
    #   value = dictionary with
    #       'used_cards' = list of used cards
    totals = {}

    # Cache the count of the cards used for each total instead of
    # computing this count during each loop iteration.
    #   key = total
    #   value = number of used_cards for this total
    card_count = {}

    iters = 0
    start_time = perf_counter()

    # Loop over all lengths of all combinations of cards_num. Note that
    # with 20+ cards, this loop is executed millions of times ... so be
    # sensitive to realtime.
    #
    # TODO: Refactor to cut the number of iterations in half by processing
    # both the combination and the unused combination in the same iteration.
    #
    for r in range(len(cards_num)+1):
        for comb in combinations(cards_num, r):
            log.debug(comb)
            iters += 1

            comb_total = sum(comb)

            # If we haven't seen this total yet, 
            # or if this comb uses more cards than the comb we found before for this total, 
            # then store the total and the comb for later printing
            if comb_total not in totals \
            or len(comb) > card_count[comb_total]:
                totals[comb_total] = {}
                totals[comb_total]['used_cards'] = comb

                # cache the card count for future comparisons
                card_count[comb_total] = len(comb)

    elapsed_time = perf_counter() - start_time
    brag_text = f"{iters:,} possible card combinations evaluated in {elapsed_time:.7f} seconds"

    return {'totals': totals, 'brag_text': brag_text}


def find_unused_cards_totals(full_deck, totals):
    """ Finds the list of unused cards and their total value """

    # Add these keys to totals
    #    'unused_cards' = list of unused cards
    #    'unused_total' = total of unused cards

    for tot in totals:

        # Use collection.Counter instead of Sets so that duplicate card
        # values are handled correctly.
        full_deck_c = Counter(full_deck)
        used_deck = Counter(totals[tot]['used_cards'])

        full_deck_c.subtract(used_deck)

        totals[tot]['unused_cards'] = sorted(full_deck_c.elements())
        totals[tot]['unused_total'] = sum(totals[tot]['unused_cards'])

    return totals


def convert_cards_str_to_nums(cards_str):
    """ Convert cards_str into a list of ints. """
    cards_num = []

    for c in cards_str.split('.'):
        if c.isnumeric():
            cards_num.append(int(c))
        else:
            log.error(f"Cards includes this non-numeric card: %s", c)
            exit(2)
    return cards_num


def sort_by_totals(totals):
    """ reverse sort by total """
    return OrderedDict(sorted(totals.items(), key=lambda x: x[0], reverse=True))


if __name__ == '__main__':

    print(f"\nExecuting outpost-calc.py ...")

    args = parse_cmd_line()
    log.debug(args)

    # Confirm that only numeric cards were provided.
    error_msg = valid_cards_syntax(args['cards_str'])
    if error_msg:
        exit(2)

    cards_num = convert_cards_str_to_nums(args['cards_str'])

    totals = find_unique_totals(cards_num)
    brag = totals['brag_text']

    totals = find_unused_cards_totals(cards_num, totals['totals'])

    totals = sort_by_totals(totals)

    for total, tup in totals.items():
        print(f"\nCards Total  = {total:4}   Used Cards = {tup['used_cards']}\n"
              f"Unused Total = {tup['unused_total']:4}   Unused Cards = {tup['unused_cards']}")

    print(f"\n{brag}\n")

    print(f"\nDone.\n")
