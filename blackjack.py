import random
from art import logo
from replit import clear

print(logo)

random.randint(0, 12)
def deal():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card



def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(player_score, dealer_score):
  if player_score == 0:
    return "Player wins with blackjack"
  elif dealer_score == 0:
    return "House wins with blackjack"
  elif player_score > 21: 
    return "Player busts, house wins"
  elif dealer_score > 21:
    return "Dealer busts, player wins"
  elif player_score > dealer_score:
    return "Player beats the house"
  elif player_score == dealer_score:
    return "Its a push"
  else:
    return "House wins"

def game():
  print(logo)

  play = input('Do you want to play blackjack?').lower()
  
  is_game_over = False
  print('Dealer stays at 17.')

  
  player_hand = []
  dealer_hand = []

  for i in range(2):
    player_hand.append(deal())
    dealer_hand.append(deal())

  deal()
  print(player_hand)
  print(dealer_hand)

  player_score = calculate_score(player_hand)
  dealer_score = calculate_score(dealer_hand)

  player = print(f"You have {player_hand} for a total of {player_score}.")
  dealer = print(f"The dealer is showing{dealer_hand[0]}.")

  
  while is_game_over == False:
    if player_score == 0 or dealer_score == 0 or player_score > 21: 
      is_game_over = True
    else: 
      player_option = input("Do you want to hit or stay?").lower()
      if player_option == 'hit':
        player_hand.append(deal())
        player_score = calculate_score(player_hand) 
        print(f"You have {player_hand} for a total of {player_score}.")
      else:
        is_game_over = True
      
    
    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal())
        dealer_score = calculate_score(dealer_hand)
        
  if is_game_over == True: 
    print(f"Your final hand is: {player_hand} which is a score of {player_score}.")
    print(f"The dealers final hand was{dealer_hand} which is {dealer_score}.")  
    print(compare(player_score, dealer_score))
 
game()

while input("Do you want to play another hand? Yes or no").lower() == 'yes':
  clear()
  game()