# USA States Quiz Game

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
![Version](https://img.shields.io/badge/version-v0.1-brightgreen)

## Overview

This is a simple Python quiz game that tests your knowledge of U.S.A. states. The game uses the Turtle graphics library to display a blank map of U.S.A. states. Users are prompted to guess the names of the states, and correct guesses are displayed on the map.

## Requirements

- Python 3.8
- `turtle` library
- `pandas` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/akumarm23/Day25-USA_Quiz.git
   cd usa-states-quiz
   ```

2. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the game:

   ```bash
   python main.py
   ```

## Files and Structure

- `main.py`: Contains the main Python code for the quiz game.
- `blank_states_img.gif`: GIF image file displaying the blank map of U.S.A. states.
- `50_states.csv`: CSV file containing state names and their corresponding x and y coordinates for the Turtle graphics.

## Usage

- Run the `main.py` script to start the quiz.
- Enter the names of U.S.A. states when prompted.
- Type "Exit" to end the quiz and see which states were missed.
- The game will save missed states to a `missed_states.csv` file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- U.S.A. states data is sourced from the `50_states.csv` file.
- Turtle graphics library is used for the visual representation of the map.

Feel free to contribute and improve this quiz game! Happy learning!
