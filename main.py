# Casino Roulette game by csilva49
from curses import ALL_MOUSE_EVENTS
import random
import os
import time
from curses.ascii import isdigit

MAX_DEPOSIT = 1000
colors = ['red', 'green', 'black']
colors_player = {
    "a": "red",
    "b": "green",
    "c": "black",
}


# deposit function


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 and amount < MAX_DEPOSIT:
                break
            else:
                print("Your deposit needs to be bigger than $0 and under $1000.")
        else:
            print("Your input value is not supported.")
    return amount


def roll_roulette():
    color_roulette = random.choices(colors, weights=(0.47, 0.06, 0.47))

    color_roulette_str = ''.join(color_roulette)
    return color_roulette_str


def main():
    balance = deposit()
    color_roulette = roll_roulette()

    play_again = True
    while True:
        bet = input("How much would you like to bet this round? $")
        if bet.isdigit():
            bet = int(bet)
            if bet > balance:
                print("You don't have enough balance for this bet.")
            else:
                color_player = input(
                    "What color would you like to bet on? (a) Red(2x), (b) Green(10x), (c) Black(2x) ").lower()
                # roll new color every game
                color_roulette = roll_roulette()
                if color_player == "a" or color_player == "b" or color_player == "c":
                    if str(color_roulette) == colors_player[color_player]:
                        print("The roulette rolled " +
                              str(color_roulette) + ", you win!")
                        # add to balance
                        if str(color_roulette) == 'green':
                            balance = balance + (bet*10)
                        else:
                            balance + bet
                    else:
                        print("The roulette rolled " +
                              str(color_roulette) + ", you lost!")
                        # substract bet
                        balance = balance - bet
                        if balance <= 0:
                            print("You don't have any more money")
                            break

                else:
                    print("This is not a valid option, the game will now end.")
                    break

                time.sleep(2)
                # clear users screen
                os.system('cls' if os.name == 'nt' else 'clear')

                play_again = input("Your new balance is $" + str(balance) +
                                   ", would you like to keep playing? (a) Yes (b) No: \n\n")
                if play_again == "b":
                    print("The game is finished, you have $" +
                          str(balance) + " left.")
                    break
                elif play_again == "a":
                    # clear users screen
                    os.system('cls' if os.name == 'nt' else 'clear')
                    color_roulette = roll_roulette()
                else:
                    print("Not a valid option, the game will end now.")
                    break
        else:
            print("Please input a valid number")


main()
