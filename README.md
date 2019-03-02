# outpost-calc
Card calculator for Outpost board game

## Outpost board game
The Outlook board game is described by [Wikipedia](https://en.wikipedia.org/wiki/Outpost_\(board_game\)) 
and [Board Game Geek](https://boardgamegeek.com/boardgame/1491/outpostsold), and 
sold by [Amazon](https://smile.amazon.com/Stronghold-Games-2003SG-Outpost/dp/B005J2RYZS/ref=smi_www_rco2_go_smi_5171374337?_encoding=UTF8&SubscriptionId=AKIAJQZPVL52RDH5YIQQ&camp=2025&creative=165953&creativeASIN=B005J2RYZS&ie=UTF8&linkCode=xm2&tag=itemtext-boardgamegeek-20) 

## Why does it need a calculator?
The goal of this calculator is to ease the burden of arithmetic in the game.

At the start of each round, each player draws cards according to the resources they have developed. These cards each have an number between 1 and 100, and the sum of these cards is a player's "buying power" for that round.

Each round, the player must add up his/her cards to determine his/her buying power. This gets tiresome, especially considering:
* No change is given for purchases, so players are motivated to find an exact mix of cards that equal the purchase price
* There is a limit of cards that a player can hold, so players are motivated to spend as many cards as possible (e.g. spend cards with values 1,4,5,7,8 instead of spending a single card with value 25.

Early in the game, a player might have less than 10 cards. Late in the game, a player can have up to 30 cards. This is when the arithmetic becomes a (debateably tiresome) burden to the players, and the pace of play slows dramatically. Wouldn't it be nice if we had a calculator that could do all the math for us?

## How does the calculator work?
After logging in, a single text box is presented with a Submit button. Enter your card values in the box, and use periods to separate each card. For example, if your hand is 1,4,5,7,8 then you will enter 1.4.5.7.8 and click Submit. The calculator will show all possible totals using these cards, which combination of cards yields this total (using the maximum count of cards), and the total of the remaining cards in your hand.

## Where did the calculator come from?
This calculator is implemented in Python and uses the Flask framework. The Flask code closely follows Miguel Grinberg's "The New and Improved Flask Mega-Tutorial" (which I highly recommend -- Miguel has a talent for simple explanations).
