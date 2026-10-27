# 📒 Contact Library — My First Python OOP Project

## About

This is my **first project using Object-Oriented Programming (OOP) in Python**. I built this simple Contact Library to practise organizing data and related functionality using a class, objects, and methods.

The program lets users enter contact names and phone numbers, display contacts stored during the current run, and search for a contact by name.

## Features

- **Add contacts:** Enter a contact name and phone number.
- **Display contacts:** Show all contacts stored while the program is running.
- **Search contacts:** Find a contact by name using case-insensitive matching.
- **Phone number validation:** Check that a phone number contains digits only and has at least 10 digits.
- **Input cleaning:** Remove leading and trailing whitespace from names and phone numbers.

## Technologies

- Python 3
- Object-Oriented Programming (OOP)

## Concepts Practised

- Classes and objects
- Constructor (`__init__`)
- Class attributes and instance attributes
- Class methods (`@classmethod`)
- Static methods (`@staticmethod`)
- Lists, loops, and conditional statements
- String methods such as `strip()` and `lower()`
- Basic input validation

## How to Run

**Requirement:** Python 3 installed on your computer.

1. Clone the repository:

   ```bash
   git clone https://github.com/ANMOL-CREATIONS/Contact-library-using-OOPs.git
   ```

2. Open the project folder:

   ```bash
   cd Contact-library-using-OOPs
   ```

3. Run the program:

   ```bash
   python ContactLibrary.py
   ```

4. Enter how many contacts you want to add, then provide each contact's name and phone number when prompted.

## Limitations

- Contacts are stored in memory and are not saved after the program closes.
- Phone number validation checks digits and minimum length only; it does not verify country codes or national numbering rules.
- The current script displays contacts at the end of the run; searching is available as a class method but is not yet exposed through an interactive menu.

## Future Improvements

- Add options to update and delete contacts.
- Prevent duplicate contacts.
- Save contacts permanently using JSON or SQLite.
- Improve input validation and exception handling.
- Add a menu-driven interface.

## Feedback Welcome 💬

Since this is my **first OOP project**, I’m still learning and improving. I’d appreciate feedback from fellow developers and experienced Python programmers.

- What would you improve in my code?
- What coding practices should I follow to make it more professional?
- Which feature should I build next?

Thanks for reviewing my project and sharing suggestions!
