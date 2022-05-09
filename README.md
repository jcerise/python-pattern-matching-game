# PEP-636 Pattern Matching Game
PEP-636 lays out a theoretical text based game as the basis for its (quite good) tutorial on structural pattern matching in python 3.10. It hints at a greater sturcture of a text based game engine.
I decided to, while learning about structural pattern matching, flesh out this framework into an actual text based game engine, which can be used for creating text based games
of any length and complexity.

This project has very little to do with structural pattern matching at this point, though the core game loop utilizes it for its main decision tree.

I may write a couple blog posts about this.

# Running the sample game
Checkout the repo
`python main.py`
(Only works on Python 3.10+)

# Creating your own game
The game definition files are simple JSON. A game consists of a series of rooms, each with a description, and one or more exits (which also have descriptions).
See `dungeon.json` for an example game.
There is currently no way to set a win condition.

# Features I would like to add
- Inventory
- Turn based combat
- Character sheets complete with various stats
- etc etc
