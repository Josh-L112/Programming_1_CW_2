# Inventory Management System
CIS1702 – Coursework 2 (Project 1)

## Overview
This project is a menu driven Inventory Management System developed using Python.
It allows users to manage inventory items by adding, viewing, searching, updating,
and deleting records. All data is stored constantly using a JSON file so that
inventory information is retained between program runs.

This system was created to meet the requirements of Project 1 and demonstrates
modular programming, input validation, and file handling.

## Features
- Add new inventory items
- View all inventory items
- Search for an item by ID
- Update item quantity and price
- Delete items from the inventory
- Persistent storage using JSON
- Input validation and error handling
- Modular and well-structured code

## Folder Structure
inventory_app/
│
├── main.py
├── inventory.py
├── models.py
├── storage.py
├── utils.py
│
└── data/
    └── inventory.json

## Requirements
- Python 3.8 and above
- No external libraries required

## How to Run
1. Open a terminal in the inventory_app folder
2. Run the program using:

python main.py

## How to Use
When the program starts, the following menu is displayed:

1. Add item
2. View items
3. Search item
4. Update item
5. Delete item
6. Exit

Enter the number corresponding to the action you want to perform and follow the
on-screen instructions.

All changes are saved automatically.

## Data Storage
Inventory data is stored in the following file:

data/inventory.json

This file is created and updated automatically by the program.

## Error Handling
- Prevents invalid input for quantities and prices
- Handles empty inventory cases safely
- Prevents crashes caused by incorrect user input

## Learning Outcomes Addressed
LO1 – Problem analysis and solution design  
LO2 – Use of appropriate programming constructs  
LO3 – Modular programming and data persistence  
LO4 – Testing, validation, and documentation
