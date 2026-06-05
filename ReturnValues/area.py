def area(length, width):
    print(str(length * width) + " square feet")
    return length * width

def main():
    house = area(10, 20)
    yard = area(50, 100)
    total = house + yard
    print(str(total) + " square feet")
    
main()