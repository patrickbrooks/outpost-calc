#!/usr/local/bin/python
#
# outpost-calc.py
#
#
import argparse
from itertools import combinations
import logging
from pprint import pprint
from sys import stdout


# Prepare a logger that prints to stdout
log = logging.getLogger(__name__)
stdout_handler = logging.StreamHandler(stdout)
stdout_handler.setFormatter(logging.Formatter('%(levelname)-8s %(message)s'))
log.addHandler(stdout_handler)


def parse_cmd_line():
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

    # Confirm that only numeric cards were provided, and create an
    # array of numbers from the given array of strings.
    cards_num = []
    cards_str = args.cards.split('.')
    for c in cards_str:
        if c.isnumeric():
            cards_num.append(int(c))
        else:
            log.error(f"Cards includes this non-numeric card: %s", c) 
            exit(2)
    
    return {
        'cards' : cards_num
    }


def find_unique_totals(cards):

    # key = total, 
    # value = dictionary with
    #    'comb_used' = list of used cards
    #    'comb_unused' = list of unused cards
    totals = {}

    # To determine the set of unused cards, subtract the used cards from 
    # the full set of cards
    full_deck = set(cards)

    iter_count = 0 # to show how hard we are working :)

    # loop over all lengths of all combinations of cards
    for r in range(len(cards)+1):
        for comb in combinations(cards, r):
            iter_count += 1
            log.debug(comb)
            
            # stuck with this 
            comb_total = sum(comb)
                
            # if we haven't seen this total yet, or if this comb uses more cards
            # than the comb we found before, then store the total and the tuple 
            # for later printing
            if comb_total not in totals \
            or len(comb) > len(totals[comb_total]):
                temp = {}
                temp['comb_used'] = comb

                unused_cards = full_deck - set(comb)
                temp['comb_unused'] = list(unused_cards)

                totals[comb_total] = temp

    print("    Total         Used Cards       Unused Cards")
    for tot, tup in sorted(totals.items(), key=lambda x: x[0], reverse=True):
        print(f"{tot:6}        {tup['comb_used']}         {tup['comb_unused']}")            
 
    print(f"\nTotal combinations evaluated = {iter_count}")

if __name__ == '__main__':

    print(f"\nExecuting outpost-calc.py ...")

    args = parse_cmd_line()
    log.debug(args)

    find_unique_totals(args['cards'])

    print(f"\nDone.\n")
