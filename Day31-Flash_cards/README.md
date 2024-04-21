# Day 31 - Flash Cards App

Flashy is a simple flashcard application built with Python and tkinter library to help users learn French vocabulary. It presents random French words and allows users to test their knowledge by flipping the card to reveal the English translation.

## Features

- **Flashcard Display**: Displays random French words with English translations.
- **Flip Card**: Allows users to flip the card to reveal the English translation.
- **Remove Word**: Allows users to remove a word from the list if they know it well.
- **Persistent Data**: Stores words to learn in a CSV file for future sessions.

## How to Use

1. **Clone Repository**: Clone this repository to your local machine.
2. **Install Dependencies**: Ensure you have Python installed on your machine. You may need to install the `tkinter` library if you haven't already.
3. **Run the Application**: Execute the `main.py` file to launch the flashcard application.
4. **Learn French Words**: Use the "Next" button to display a new French word, and click the "Right" or "Wrong" button to indicate your understanding.
5. **Remove Known Words**: If you know a word well, click the "Right" button to remove it from the list of words to learn.
6. **Review Words**: Repeat the process to review and learn new French words effectively.

## Files

- **main.py**: Contains the main application code.
- **words_to_learn.csv**: Stores the words to learn in CSV format.
- **french_words.csv**: Backup file containing initial French words for learning.
- **images**: Directory containing images used in the GUI.

## Dependencies

- Python (>=3.6)
- tkinter (Python GUI library)
- pandas (Python Data Analysis Library)
