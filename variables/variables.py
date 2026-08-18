def get_guess():
    guess = int(input("Enter your guess: "))
    return guess



def main():
    guess = get_guess()
    if guess == 50:
        print("Congratulations! You guessed the correct number.")
    else:
        print("Sorry, that's not the correct number. Try again!")
    

main()