import random

def roll_dice(num_dice, num_sides):
    rolls = []
    total = 0
    for _ in range(num_dice):
        roll = random.randint(1, num_sides)
        rolls.append(roll)
        total += roll
    return rolls, total

def main():
    num_dice = int(input("Enter the number of dice: "))
    num_sides = int(input("Enter the number of sides per die: "))

    rolls, total = roll_dice(num_dice, num_sides)

    print("Results of each roll:")
    for i, roll in enumerate(rolls):
        print(f"Die {i + 1}: {roll}")
    print(f"Total sum of all dice: {total}")

    reroll_option = input("Would you like to reroll some or all of the dice? (yes/no): ").lower()
    if reroll_option == "yes":
        reroll_dice = input("Enter the indices of the dice you want to reroll (e.g., 1 3 5), or 'all' to reroll all dice: ")
        if reroll_dice == "all":
            rolls, total = roll_dice(num_dice, num_sides)
        else:
            reroll_indices = [int(idx) - 1 for idx in reroll_dice.split()]
            for idx in reroll_indices:
                rolls[idx] = random.randint(1, num_sides)
            total = sum(rolls)
        print("Results of reroll:")
        for i, roll in enumerate(rolls):
            print(f"Die {i + 1}: {roll}")
        print(f"Total sum of all dice after reroll: {total}")

if __name__ == "__main__":
    main()
