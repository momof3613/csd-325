
# Ajanae Stanback
# CSD325 - Advanced Python
# Assignment 1.3: On the Wall
# Purpose: Count down bottles of beer using a function.


def countdown(bottles):
    """Display the bottle countdown from the starting number to one."""
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall,")
        print(f"{bottles} bottles of beer.")
        print("Take one down, pass it around.")

        bottles -= 1

        if bottles == 1:
            print("1 bottle of beer on the wall.\n")
        else:
            print(f"{bottles} bottles of beer on the wall.\n")

    if bottles == 1:
        print("1 bottle of beer on the wall,")
        print("1 bottle of beer.")
        print("Take one down, pass it around.")
        print("No more bottles of beer on the wall.\n")


def main():
    """Ask for a bottle count and start the countdown."""
    try:
        bottles = int(input("How many bottles of beer are on the wall? "))

        if bottles > 0:
            countdown(bottles)
            print("Time to buy more beer!")
        else:
            print("Please enter a number greater than zero.")
    except ValueError:
        print("Please enter a valid whole number.")


if __name__ == "__main__":
    main()
