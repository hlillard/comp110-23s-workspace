"""Demonstrates how to Count Something"""
number_string: str = "321"

#if a number % 2 == 1, then it is odd
if (int(number_string[0]) % 2 == 1 ):
    number_of_odds = number_of_odds + 1
if (int(number_string[1]) % 2 == 1 ):
    number_of_odds = number_of_odds + 1
if (int(number_string[2]) % 2 == 1 ):
    number_of_odds = number_of_odds + 1

print("You have " + str(number_of_odds) + "odds in the string!")