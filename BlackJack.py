# Two players are gonna play the game, one will be computer
# Player 2 can choose if he/she want to hit or pass
# Goal is to get near 21 but not to go over 21:: if sum of values of cards goes above 21, then it is bust and computer wins
# Player 2 or P2 can place bet on one hand of black jack
# if the sum of card value is exactly 21, then it is blackjack and p2 gets 1.5X money
# class required to record attributes like bank_bal for p2
# 1 can be treated as a 1 or a 11

import random
import time
from IPython.display import clear_output


class Player():
    ''' class to get player 2 details '''

    def __init__(self, amount):
        self.amount = amount

    def manage_ac(self, val):
        self.amount = self.amount+val
        print(self.amount)
        return self.amount


def hit(): return deck.pop()


def stay(com_cards):
    ''' when player does not want to hit anymore then computer gets its turn '''
    while(sum(com_cards) < 17):
        com_cards.append(hit())
    return com_cards  # returning list of cards for computer

# computer dealer will distribute two cards to player and two to itself, but will display only one card


def card_dist(): return [deck.pop(), deck.pop()]


def bust_check(card_list): return sum(card_list) > 21


def check_aces(pl_cards):
    if(1 in pl_cards and (sum(pl_cards)+10) <= 21):
        pl_cards[pl_cards.index(1)] = 11
    return pl_cards


def black_check(pl_cards):
    ''' to blackjack check '''
    pl_cards = check_aces(pl_cards)
    return (sum(pl_cards) == 21)


# gameplay design: user must provide the details like how much amount to put on the table: then we will call the class
print('Player please enter the amount on the table :: ')
p2 = Player(int(input()))  # initializer will assign amount for p2

# Create a deck of 52 cards
deck = [10 if(v >= 11) else v for v in range(1, 14)]*4
random.shuffle(deck)  # shuffle the deck

# _______________________________________________###_______________________________________________#
play = True
while play:
    # to store the cards that player gets at the begining of the game
    pl_cards = []
    pl_cards = card_dist()

    # computer also gets the cards now
    com_cards = []
    com_cards = card_dist()

    # placing bet by player
    while True:
        print('Please enter the bet amount :: ')
        bet = int(input())
        # this will reduce the amount from the class attribute:: adding the money back in next line
        bal_check = p2.manage_ac(-bet)
        p2.manage_ac(bet)
        clear_output()
        if(bal_check < 0):
            print('Not enough funds :: Try again please!')
            continue
        else:
            break
    clear_output()

    # creating flow of choice for hit and stay
    # for initially displaying cards of both computer dealer and player
    print('Computer :: ')
    print(com_cards[1])
    print('Player :: ')
    print(pl_cards)

    # checking if p2 has hit the blackjack
    if(black_check(pl_cards)):
        print('BlackJack. You have won!')
        p2.manage_ac(2.5*bet)  # added the bet money
        print('Updated Balance :: {}'.format(p2.amount))
        # asking if player wants to play again
        print('Want to play again (Y/N) :: ')
        play = True if(input() == 'Y') else False
        continue
    clear_output()
#_____________________________________________________________________________________________#
    choice = True
    black_flg, bust_flg = False, False
    while choice:
        print('Computer :: ')
        print(com_cards[1])
        print('Player :: ')
        print(pl_cards)

        print('Do you want to hit? (Y/N) ::')
        choice = True if(input() == 'Y') else False
        if choice:  # if player decides to hit()
            pl_cards.append(hit())
            if(bust_check(pl_cards)):
                print('Busted. You have lost!')
                time.sleep(3)
                # in case of bust, bet is passed as negative number
                p2.manage_ac(-bet)
                print('Updated Balance :: {}'.format(p2.amount))
                bust_flg = True
                break
            elif(black_check(pl_cards)):
                print('BlackJack. You have won!')
                p2.manage_ac(1.5*bet)  # added the bet money
                print('Updated Balance :: {}'.format(p2.amount))
                black_flg = True
                break
            clear_output()
        else:
            # when p2 decides to stay then computer has to hit until 17 or more
            com_cards = stay(com_cards)
            if(bust_check(com_cards)):
                print('Computer busted. You have won!')
                p2.manage_ac(bet)  # added the bet money
                print('Updated Balance :: {}'.format(p2.amount))
                bust_flg = True
                break
#_________________________________________________________________________________________#
    print('Computer :: ')
    print(com_cards)
    print('Player :: ')
    print(pl_cards)
    if(black_flg == False and bust_flg == False):
        # checking if any aces can give us more value
        pl_cards = check_aces(pl_cards)
        if(sum(com_cards) > sum(pl_cards)):
            print('You have lost!')
            time.sleep(3)
            # in case of bust, bet is passed as negative number
            p2.manage_ac(-bet)
            print('Updated Balance :: {}'.format(p2.amount))
        elif(sum(com_cards) < sum(pl_cards)):
            print('You have won!')
            p2.manage_ac(bet)  # added the bet money
            print('Updated Balance :: {}'.format(p2.amount))
        else:
            print('It is a tie')
    print('Want to play again (Y/N) :: ')
    play = True if(input() == 'Y') else False
# Finished on 23-May-2020
