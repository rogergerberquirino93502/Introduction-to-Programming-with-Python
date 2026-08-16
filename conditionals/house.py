name = input("What is your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Hello, " + name + "! Welcome to the house of Gryffindor.")
    case "Draco":
        print("Hello, " + name + "! Welcome to the house of Slytherin.")   
    case "Luna":
        print("Hello, " + name + "! Welcome to the house of Ravenclaw.")
    case "Cedric":
        print("Hello, " + name + "! Welcome to the house of Hufflepuff.")
    case _:
        print("Hello, " + name + "! Welcome to Hogwarts.")