# Blackjack Project
This is a simple implementation of the popular card game Blackjack. The project provides a command-line interface for playing the game.

## Rules
The following are the house rules for this implementation of Blackjack:

* The deck used is unlimited in size.
* There are no jokers in the deck.
* The cards Jack, Queen, and King all count as 10.
* The Ace can count as either 11 or 1, depending on the player's choice.
* The deck of cards used in the game is: [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10].
* Cards are not removed from the deck as they are drawn.

## How to Play
To play the game, you need to run the play_game() function. The game will start by dealing two cards each to the player and the computer. You will be prompted to either draw another card or pass. The computer will automatically draw cards until its score is at least 17. Once both players have completed their turns, the scores will be compared to determine the winner.

**You can restart the game by typing 'y' when prompted at the end of a game.**

Have fun playing Blackjack!
