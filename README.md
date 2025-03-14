# U.S. States Game

## Description
This is an interactive U.S. states guessing game built using Python's `turtle` and `pandas` libraries. The game presents a blank map of the United States, and the user must input state names. Correct guesses will be displayed on the map in their respective locations. The game continues until all 50 states are guessed or the user exits the game.

## Features
- Interactive game interface using `turtle` graphics.
- Keeps track of correctly guessed states.
- Saves unguessed states to a `missing_state.csv` file when the user exits.
- Displays guessed states on the map in their correct locations.

## How to Run
1. A map of the U.S. will appear. Enter state names in the prompt.
2. Correct guesses will be displayed on the map.
3. Type `Exit` to quit the game and generate a list of missing states in `missing_state.csv`.

## Example Output
- If the user correctly guesses "California", the name appears at the correct coordinates on the map.
- If the user exits before completing all 50 states, a file `missing_state.csv` is generated with the unguessed states.




