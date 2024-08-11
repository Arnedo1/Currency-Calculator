Cs50p Final project
# Currency Calculator
### Video Demo: https://youtu.be/buB2LwwFYpE
### Definition

This program calculates whatever currency you want to calculate against your favorite currencys.

How the Program Works?
The Program when starts, its starts with a starting favoriteslist of currencys calculated against 1 dollar.
The program then promts you if you whatyou want to do.

To caluculate, you type in the number 1 when asked 'Enter option: '. Then the program will ask you for a currency.
If you type a currency thats exists the program wil ask you for a amount. If this is a valid amount the program wil calculate all the
currencys in the favorites list agains the currency and amount you have given.

To add a currency to the favorites list. You type in '2' when asked 'Enter option:'. Then you have to type a valid currency code.
It doesnt matter if you use lower case or uppercase it just has to be a currency code that exists. If you type in something that
is not a valid currency code the program will print the text: ... is not a valid currency code. And if the currency code is allready in the
current favorites list. The program will print: ... is already in the favorites list

To remove a currency from the favorites list. You type in '3' when asked 'Enter option:'. Then you have to type a currency code that
is in the current favorites list. It doesnt matter if you use lower case or uppercase it just has to be in hte current list.

To quit the program you have to type '4' when asked 'Enter option:'. Afther this you see the message 'Quitting program'.

Installation
It's recommended to first create a python virtual environment and then install the requirements with the following command:

pip3 install -r requirements.txt
Then run the command:

python project.py

Main files
project.py - main file with the calculator
test_project.py - four tests that test the program's functions

