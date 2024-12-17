import random
import time

playAgain = True
totalLoan = 0
loan = 0
file = open("blackjackMoney.txt", "r")
money = int(file.read())
file.close()
startingMoney = money
print(money) 
#betting system
def betting(): 
    global money
    global bet
    global totalLoan
    while True:
        
        if money == 0:
            print("You are out of money!")
            loan = int(input("Would you like to take out a loan, if yes insert the loan amount: "))
            totalLoan += loan
            money += totalLoan

        bet = int(input("Insert your bet amount: "))
        # bet inbetween 0 and thier money
        if 0 < bet <= money:
            money = money - bet
            print("Your new balance is:", money, "\n\n")
            break
        else:
            print("You cannot afford this bet")

#create a deck with all 52 cards
def createDeck():
    global deck, player_cardsList, dealer_cardsList
    suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
    values = range(1,14)

    deck = {}
    player_cardsList = []
    dealer_cardsList = []

    #iterate through all cards and give them values (fix ace)
    for suit in suits:
        for value in values:
            if value == 1:
                deck[f'Ace of {suit}'] = 11
            elif value == 11:
                deck[f'Jack of {suit}'] = 10
            elif value == 12:
                deck[f'Queen of {suit}'] = 10
            elif value == 13:
                deck[f'King of {suit}'] = 10
            else:
                deck[f'{value} of {suit}'] = value

#deal one card to the player
def dealCard():
    global playerHand
    #get a random card from a list of cards
    card = random.choice(list(deck.keys()))
    #get the value
    cardKey = deck.get(card)

    #remove
    deck.pop(card)

    #add it to the lists
    player_cardsList.append(card)
    player_cardsKeys.append(cardKey)
    playerHand += cardKey

#deal one card to the dealer
def dealDealerCard():
    global dealerHand
    #random card and value
    card = random.choice(list(deck.keys()))
    cardKey = deck.get(card)

    deck.pop(card)

    #add to list
    dealer_cardsList.append(card)
    dealer_cardsKeys.append(cardKey)
    dealerHand += cardKey


def displayPlayerCards():
    global player_cardsList, playerHand

    print("Your Cards: ")

    for card in range(len(player_cardsList)):
        #if card is not the last card end with ", "
        if card != (len(player_cardsList) -1):
            print(player_cardsList[card], end=", ")
    
        #if it is the last dont add the ", " instead make new line
        else:
            print(f'{player_cardsList[card]}')
    
    print(f'You have a {playerHand} in your hand!\n')

def displayDealercards():
    global dealer_cardsList

    print("Dealers Cards: ")
    for card in range(len(dealer_cardsList)):
        #only print the first card
        if card == 0:
            print(dealer_cardsList[card], end=", ")
    
        elif card != (len(dealer_cardsList) - 1):
            print("???", end=", ")

        #dont add comma for the last card
        else:
            print("???")
    print('')

def displayEveryCard():
    displayPlayerCards()

    global dealer_cardsList, dealerHand
    
    print("Dealers Cards: ")
    
    for card in range(len(dealer_cardsList)):

        #if its not the last card use comma
        if card != (len(dealer_cardsList) -1):
            print(dealer_cardsList[card], end=", ")
        #no comma
        else:
            print(f'{dealer_cardsList[card]}')
    print(f"The dealer has a {dealerHand} in their hand\n")

def loanPayments():
    global totalLoan, money, bet
    if totalLoan > 0:
            print(f"You currently have a loan of ${totalLoan}, half off your winnings go toward paying this loan")
            if totalLoan > bet:
                money -= bet
                totalLoan -= bet
                print(f"You are now at ${money}, and still have a loan of ${totalLoan}")
            else:
                money -= totalLoan
                totalLoan = 0
                print(f"You are now at {money}, and your loan is fully paid off!")
#game loop!
while playAgain:
    bet = 0
    playerHand = 0
    dealerHand = 0
    player_cardsList = []
    player_cardsKeys = []
    dealer_cardsList = []
    dealer_cardsKeys = []
    deck = {}
    playerTurn = ''
    dealerTurn = ''
    result = ''
    

    createDeck()
    
    betting()

    dealCard()
    dealDealerCard()
    dealCard()
    dealDealerCard()

    displayPlayerCards()
    displayDealercards()
    
    
    while playerTurn != 's':
        print("Hit or Stand(h / s)")
        playerTurn = input("")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        
        if playerTurn.lower() == 'h':
            dealCard()
            if playerHand > 21:
                i = 0
                for key in player_cardsKeys:
                    i += 1
                    if key == 11:
                        playerHand -= 10
                        player_cardsKeys[i-1] = 1
            displayPlayerCards()
        elif playerTurn.lower() == 's':
            #do dealer turn
            continue
        else:
            print("That is not a vaild input >:{")

        
        if playerHand > 21:    
            dealerTurn = 'over'
            result = "lose"
            break
    
    while dealerTurn != 'over':
        if dealerHand < 17:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            dealDealerCard()
            displayDealercards()
        elif dealerHand < 22:
            dealerTurn = 'over'
        else:
            dealerTurn = "over"
            result = "win"
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
    displayEveryCard()

    
    if result == "lose":
        print("Bust, your hand is over 21")
        print(f"You are down to ${money}")

    elif result == "win":
        print("Dealer Bust, you win")
        money += (bet * 2)
        print(f"You have won ${bet * 2}, with a new balance of ${money}")
        loanPayments()

    elif playerHand > dealerHand:
        print("You win, your hand is larger than the dealers")
        money += (bet * 2)
        print(f"You have won ${bet * 2}, with a new balance of ${money}")
        loanPayments()
    
    elif playerHand < dealerHand:
        print("You lose, your hand is smaller than the dealers")
        print(f"You are down to ${money}")
    
    elif playerHand == dealerHand:
        print("Draw, your hand has the same value as the dealers")
        money += bet
        print(f"Your balance is unchanged at ${money}")
    
    #play again if input == y, else end
    playAgain = input("Do you want to play again(y, n): ").lower() == "y"
    

print(f"You started with ${startingMoney} and you now have ${money}, this is a profit of ${money - startingMoney}!")
file = open("blackjackMoney.txt", "w")
file.write(str(money))
file.close()