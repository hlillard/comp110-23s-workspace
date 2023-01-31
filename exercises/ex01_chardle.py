"""Ex01 - Chardle - A cute step toward Wordle."""

__author__ = "730476613"

five_word : str = input("Choose a five-letter word: ")
if(len(five_word) != 5):
    print("Error: Word must contain 5 characters")
    exit()
one_letter: str = input ("Choose a letter: ")
print("Searching for " + one_letter + " in " + five_word)
if(len(one_letter) != 1):
    print("Error: Letter must be a single character.")
    exit()
count_inst : int = 0

if(five_word[0] == one_letter):
    print(one_letter + " found at index 0")
    count_inst = count_inst + 1
if(five_word[1] == one_letter):
    print(one_letter + " found at index 1")
    count_inst = count_inst + 1
if(five_word[2] == one_letter):
    print(one_letter + " found at index 2")
    count_inst = count_inst + 1
if(five_word[3] == one_letter):
    print(one_letter + " found at index 3")
    count_inst = count_inst + 1
if(five_word[4] == one_letter):
    print(one_letter + " found at index 4")
    count_inst = count_inst + 1

if(count_inst == 0):
    print("0 instances of " + one_letter + " found in " + five_word)
if(count_inst == 1):
    print("1 instance of " + one_letter + " found in " + five_word)
if(count_inst == 2):
    print("2 instances of " + one_letter + " found in " + five_word)
if(count_inst == 3):
    print("3 instances of " + one_letter + " found in " + five_word)
if(count_inst == 4):
    print("4 instances of " + one_letter + " found in " + five_word)
if(count_inst == 5):
    print("5 instances of " + one_letter + "found in " + five_word)


                  

             

