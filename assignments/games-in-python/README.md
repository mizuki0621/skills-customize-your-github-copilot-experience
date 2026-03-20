
# 📘 Assignment: Games in Python

## 🎯 Objective

Practice core Python programming skills by building a simple Hangman-style game. In this assignment, you will work with strings, loops, conditionals, lists, and user input to create an interactive program.

## 📝 Tasks

### 🛠️ Set Up the Hangman Game

#### Description
Create the basic structure of a Hangman game. Your program should choose a word from a predefined list and display the hidden word using underscores so the player can begin guessing.

#### Requirements
Completed program should:

- Store several possible words in a predefined list.
- Randomly select one word for the game.
- Display the word as underscores, with one underscore for each letter.
- Ask the player to enter a letter guess.
- Keep track of the letters the player has already guessed.

Example display:

```text
Word: _ _ _ _ _
Guess a letter: a
```

### 🛠️ Complete the Game Logic

#### Description
Finish the game so the player can keep guessing letters until they either reveal the full word or run out of incorrect guesses.

#### Requirements
Completed program should:

- Reveal correctly guessed letters in the correct positions.
- Decrease the number of remaining attempts when the player guesses incorrectly.
- Show the current progress after each guess.
- End the game with a win message if the player guesses the full word.
- End the game with a lose message if the player uses all attempts.

Example outcome:

```text
Word: p y t h o n
You win!
```
