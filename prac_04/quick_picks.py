import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("That makes no sense!")
        number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        quick_pick = generate_quick_pick()
        display_quick_pick(quick_pick)


def generate_quick_pick():
    """Generate a single quick pick."""
    quick_pick = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in quick_pick:
            number = random.randint(MINIMUM, MAXIMUM)
        quick_pick.append(number)
    quick_pick.sort()
    return quick_pick


def display_quick_pick(quick_pick):
    """Display a single quick pick."""
    print(" ".join(f"{number:2}" for number in quick_pick))

main()
