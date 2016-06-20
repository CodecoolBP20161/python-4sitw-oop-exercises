# Phone number database

## Description
In this exercise, you should write a simple application that can help you search for the owner of a phone number.

## User stories (required)
- As a User, I'd like to enter a full phone number (with non-correct punctuations), to get the name of the owner of that number.
- As an Administrator, I'd like to change the phone number database without writing into Python code

## Extra feature's user story (optional)
- As a User, I'd like to enter the beginning of a phone number (with non-correct punctuations) to get a list of possible owners

## Example output
```
user@computer:$ python phone_numbers.py ./phone_data_10000.csv
Please enter the phone number: 046162276
This number belongs to: Ka Sturdy

user@computer:$ python phone_numbers.py ./phone_data_10000.csv
Please enter the phone number: 999999
No match found.

user@computer:$ python phone_numbers.py
No database file was given.
```

## What the application should do?
1. Read the .csv file (given first parameter)
1. Create Person instances from each name-number pair
1. Store the Person objects in a list
1. Ask the user for a phone number
1. Find the owner of the given phone number
1. Print out the result of the search
