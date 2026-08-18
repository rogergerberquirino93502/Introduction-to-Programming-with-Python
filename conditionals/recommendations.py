def main():
    difficulty = input ("Difficult or Casual?")
    players = input ("Multiplayer or Singleplayer?")

    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Poker")
        elif players == "Singleplayer":
            recommend("Klondike")
        else:
            print("Enter a valid number of players!")
    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommend("Hearts")
        elif players == "Singleplayer":
            recommend("Clock")
        else:
            print("Enter a valid number of players!")
    else:
        print("Enter a valid difficulty!")


def recommend(game):
    print("We recommend you play ", game)


main()