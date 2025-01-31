# Closure is a function having access to the scope of its
# parent function even after the parent function has returned.

def parent_function(person, coins):
    # coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left")
        else:
            print("\n" + person + " has no coins left")

    return play_game


tommy = parent_function("Tommy", 5)
jenny = parent_function("Jenny", 2)

tommy()
tommy()
jenny()
tommy()
