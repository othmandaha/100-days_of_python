# Day 30 - Json & Exeptions (Password Manager improved)

This is a simple password manager application built using Python's Tkinter library. It allows users to generate, save, and retrieve their passwords for different websites.

## Features
- **Password Generation**: Users can generate secure passwords consisting of letters (both uppercase and lowercase), numbers, and symbols.
- **Save Passwords**: Users can input their website, email/user, and password information and save it for future reference.
- **Search Functionality**: Users can search for previously saved passwords by entering the website name.

## Data Storage
The saved passwords are stored in a JSON file named `data.json`. Each entry contains the website as the key and the corresponding email/user and password information as the value.

## Usage
1. Run the script `password_manager.py`.
2. Use the "Generate Password" button to generate a secure password or enter your own password.
3. Fill in the website, email/user (optional), and password information.
4. Click on the "Add" button to save the information.
5. To search for a password, enter the website name in the search field and click "Search".

## Dependencies
- Python 3.x
- Tkinter (Python's standard GUI library)
- pyperclip (for copying generated passwords to clipboard)

## File Structure
- `password_manager.py`: Python script containing the password manager application.
- `data.json`: JSON file to store the saved passwords.
- `logo.png`: Image file for branding purposes.

