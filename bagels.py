"""Bagels, A deductive logic game where you must
guess a number based on clues."""
import random

# delaring global variables
random_number = random.randint(0, 999)
secret_number = str(random_number).zfill(3)

def check_input(value1, value2):
    """ Function checks if two strings of 3 digits containing comman digits

    Args:
        value1 (str): The first string of digits to compare
        value2 (str): The second string of digits to compare

    Returns:
        True: if value1 and value2 containing the same digits
        False: otherwise
    """
    index1 = same_position = not_same_position = 0
    saved_positions = []
    for c1 in value1:
        index2 = 0
        for c2 in value2:
            if index2 in saved_positions:
                index2 += 1
                continue
            if c1 == c2 and index1 == index2:
                same_position += 1
                saved_positions.append(index2)
                break
            elif c1 == c2 and index1 != index2:
                not_same_position += 1
                break
            index2 += 1
        index1 += 1

    # printing the appropriate message
    if same_position == 3:
        print("You got it!")
        print("Do you want to play again? (yes or no)")
        return True
    elif same_position < 3 and same_position > 0:
        for i in range(same_position):
            print("Fermi", end=" ")
        print()
    if not_same_position == 0 and same_position == 0:
        print("Bagels")
    elif not_same_position > 0:
        for i in range(not_same_position):
            print("Pico", end=" ")
        print()
    return False

i = 1
status = False

print("""Bagels, a deductive logic game.
By Adnane J adnan.jahbli@gmail.com
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:     That means:
    Pico        One digit is correct but in the wrong position.
    Fermi       One digit is correct and in the right position.
    Bagels      No digit is correct.
I have thought up a number.
You have 10 guesses to get it.""")

while i <= 10:
    try:
        print("Guess #{}".format(i))
        user_input = input("> ")
        if len(user_input) != 3 or not int(user_input):
            raise ValueError
        else:
            status = check_input(secret_number, user_input)
            if status:
                user_input2 = input("> ")
                if user_input2 in ("no", "No"):
                    print("Thanks for playing!")
                    break
                elif user_input2 in ("yes", "Yes"):
                    i = 1
                    random_number = random.randint(0, 999)
                    secret_number = str(random_number).zfill(3)
                    continue
                else:
                    print("Invalid entry, try again later!")
                    break
    except ValueError:
        print("Please enter a number of 3 digits!")
        continue
    finally:
        if not status:
            i += 1

if not status:
    print(f"Unfortunatly you lost :( the secret number was: {secret_number}")