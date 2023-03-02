"""Ask user for number, give hints about number if wrong."""

SECRET: int = 10
guess: int = int(input("Guess a Number! "))
playing: bool = True

while playing:
    if guess == SECRET:
        print("Correct! You did it! Believe in your dreams bitch <3  ")
        playing = False
    else: 
        if guess % 2 == 1:
            print("Your guess is odd. This bitch is even. ")
        if guess < SECRET:
            print("Too low Bitch! ") 
        else: 
            if guess > SECRET:
             print("Now you done went too far bitch! ")
        guess = int(input("Wrong guess. Bitch. Dumbass. Try again idiot. If you even can. Stupid. "))