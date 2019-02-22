#!/usr/local/bin/python
#
# outpost-calc.py
#
# https://stackoverflow.com/questions/464864/how-to-get-all-possible-combinations-of-a-list-s-elements
# https://docs.python.org/3/library/itertools.html
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

    # Confirm that only numeric cards were provided
    cards = args.cards.split('.')
    for c in cards:
        if not c.isnumeric():
            log.error(f"Cards includes this non-numeric card: %s", c) 
            exit(2)
    
    return {
        'cards' : cards
    }




def find_unique_totals(cards):

    # key = total, 
    # value = the combination of cards that produces this total using maximum count of cards
    totals = {}

    # loop over all lengths of all combinations of cards
    for r in range(len(cards)+1):
        for comb in combinations(cards, r):

            log.debug(comb)
            
            comb_total = 0
            for n in comb:
                comb_total += int(n)  
                
            # if we haven't seen this total yet, or if this comb uses more cards,
            # then store the total and the tuple for later printing
            if comb_total not in totals \
            or len(comb) > len(totals[comb_total]):
                totals[comb_total] = comb


    print("    Total     Cards")
    for tot, tup in sorted(totals.items(), key=lambda x: x[0], reverse=True):
        print(f"{tot:6}    {tup}")            
 

if __name__ == '__main__':

    print(f"\nExecuting outpost-calc.py ...")

    args = parse_cmd_line()
    log.debug(args)

    find_unique_totals(args['cards'])

    print(f"\nDone.\n")
