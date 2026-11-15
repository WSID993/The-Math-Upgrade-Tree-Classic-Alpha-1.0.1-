import time

nn = 0.0
Unn = 0.01

# The index 2, 3, and 4 are used as the purchase counts for UP2, UP3, and UP4 respectively
UP_List = [0, 0, 0, 0, 0, 0, 0]

while True:
    nn += Unn
    time.sleep(1)
    print(f"Current value of nn: {nn:.2f}")

    # UP2 is available only if the condition is met and UP2 has not been purchased yet
    if round(nn, 2) >= 0.10 and UP_List[2] == 0:
        choice = input("The UP2 is ready to buy (Cost: 0.10). Want to buy it? (Y/N): ").upper()
        if choice == 'Y':
            print("UP2 purchased!")
            nn -= 0.10
            Unn *= 2
            UP_List[2] += 1
        else:
            print("Purchase cancelled.")

    # UP3 is available only if UP2 has been purchased and UP3 has not been purchased yet
    if round(nn, 2) >= 0.20 and UP_List[2] == 1 and UP_List[3] == 0:
        choice = input("The UP3 is ready to buy (Cost: 0.20). Want to buy it? (Y/N): ").upper()
        if choice == 'Y':
            print("UP3 purchased!")
            nn -= 0.20
            Unn *= 1.5
            UP_List[3] += 1
        else:
            print("Purchase cancelled.")

    # UP4 is available only if UP3 has been purchased and UP4 has not been purchased yet
    if round(nn, 2) >= 0.30 and UP_List[3] == 1 and UP_List[4] == 0:
        choice = input("The UP4 is ready to buy (Cost: 0.30). Want to buy it? (Y/N): ").upper()
        if choice == 'Y':
            print("UP4 purchased!")
            nn -= 0.30
            Unn *= 2
            UP_List[4] += 1
        else:
            print("Purchase cancelled.")

    # UP5 is available only if the condition is met and UP5 has not been purchased yet
    if round(nn, 2) >= 0.50 and UP_List[5] == 0:
        choice = input("The UP5 is ready to buy (Cost: 0.50). Want to buy it? (Y/N): ").upper()
        if choice == 'Y':
            print("Game reset!")
            UP_List[5] += 1
            Unn *= 2
        else:
            print("Purchase cancelled.")
    # UP6 is available only if UP5 has been purchased and UP6 has not been purchased yet
    if round(nn, 2) >= 1.00 and UP_List[5] == 1 and UP_List[6] == 0:
        choice = input("The UP6 is ready to buy (Cost: 1.00). Want to buy it? (Y/N): ").upper()
        if choice == 'Y':
            print("UP6 purchased!")
            nn -= 1.00
            Unn *= 3
            UP_List[6] += 1
        else:
            print("Purchase cancelled.")