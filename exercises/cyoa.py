"""Five Nights at Freddy's Dating Simulator."""

__author__ = "730476613"

if __name__ == "__main__":
  main()


points: int = 0
player: str = str(input("Welcome to Freddy Fazbear's Pizzeria! How shall we introduce you to the animatronics? "))

def main() -> None:
  """Five Nights of Falling in Love."""
  global points
  global player
  greet()
  bonnie: str = input(f"{player}, it's time to meet your first option: Bonnie! He is tall, handsome, and so blue that he doesn't belong to you! Your job is to pick the date you think Bonnie would enjoy most. If correct, you will be able to have the night of your life. If you pick wrong, Bonnie will be the one that got away. Now choose: Laser Tag or Go Karts?")
if bonnie == "Laser Tag":
        print("Congrats! You an Bonnie hit it off and after a steady 4 year relationship, get married and give birth to some freaky animatronic rabbit-human hybrids!")
        exit()
if bonnie == "Go Karts":
    print("I'm sorry! Bonnie is actually terrified of cars. When you suggest this, he has flashbacks and ends up eating you in a fit of rage! Let's try the next contestant.")
    chica: str = input(f"{player}, it's time to meet your next option: Chica! She is beauty, she is grace! Which date do you think she would enjoy most: Painting or Baking?")            if chica == "Baking":
    print("Congrats! You and Chica hit it off and after a steady 4 year relationship, get married and give birth to some freaky animatronic human-chicken hybrids!")
        exit()
    if chica == "Painting":
        print("I'm sorry! Chica has suffered a lot of trauma from children painting on her! She bites off your head! Let's try again!")
             foxy: str = input(f"{player}, it's time to meet your next option: Foxy! He is ready to sail the seven seas with you! Which date do you think he would enjoy most: Swimming or Movie?")
                if foxy == "Swimming":
                    print("Congrats! You and Foxy hit it off and after a steady 4 year relationship, get married and give birth to some freaky animatronic human-fox hybrids!")
                    exit()
                 if foxy == "Movie":
                    print("I'm sorry! Foxy hates the dark and stabs his hook through your eye! Let's try one more time!")
                    freddy: str = input(f"{player}, it's time to meet your last option: He is ready to give you the best cuddles! Which date do you think he would enjoy most: Pizza or Sup Dogs?")
                    if freddy == "Pizza":
                    print("Congrats! You and Chica hit it off and after a steady 4 year relationship, get married and give birth to some freaky animatronic human-chicken hybrids!")
                    exit()
                    if freddy == "Sup Dogs":
                     print("I'm sorry! Freddy literally owns a pizza shop! He crushes you in a bear hug!")
                     print("Given you have exhausted all your options, I think it's best if we just say GAME OVER!")
                     exit()