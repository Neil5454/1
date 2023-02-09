# Blackjack Project
# features to be added: book strategy hints; handle aces; splits

import os, random, time
from art import logo

def deal_one_card():
  global card_counter
  one_card = shoe[card_counter]  # each card dealt corresponds with position in shoe (i.e., first card dealt is position "0" in shoe, second card dealt is position "1" in shoe, etc)
  card_counter += 1
  return one_card

def your_actions():
  your_cards.append(deal_one_card())
  global your_total  #setting variable as global so it can be used in 'determine winner' function
  your_total = sum(your_cards)
  print(f"Your cards: {your_cards}, current score: {your_total}")
  if your_total > 21:
    print("You bust. Dealer wins.")
  elif your_total <= 21:
    hit_or_stand = input("Do you want to hit or stand. Type 'h' or 's'. ")
    if hit_or_stand == 'h':
      return your_actions()
    if hit_or_stand == 's':
      return dealer_actions()

def dealer_actions():
  global dealer_total  #setting variable as global so it can be used in 'determine winner' function
  while dealer_total < dealer_hits_soft:
    dealer_cards.append(deal_one_card())
    dealer_total = sum(dealer_cards)
    print(f"Dealer hits.  Dealer cards: {dealer_cards}, current total: {dealer_total}")
    if dealer_total > 21:
      print("Dealer busts.  You win.")
      break
  else:
    print(f"Dealer stands.  Dealer cards: {dealer_cards}, current total: {dealer_total}")
    determine_winner()

def determine_winner():
  if dealer_total > 21:
    return print("Dealer busts.  You win.")
  elif dealer_total == your_total:
    return print("Tie.")
  elif dealer_total > your_total:
    return print("Dealer wins.")
  elif dealer_total < your_total:
    return print("You win.")

def blinking_ellipses(text, delay=0.5):
  print(end=text)
  n_dots = 0
  n_sets_ellipses = 0
  while n_sets_ellipses < 2:
    while n_dots == 3:
      print(end='\b\b\b', flush=True)
      print(end='   ', flush=True)
      print(end='\b\b\b', flush=True)
      n_dots = 0
      n_sets_ellipses += 1
    else:
      print(end='.', flush=True)
      n_dots += 1
    time.sleep(delay)
  else:
    os.system('clear')


answer = input("Do you want to play a game of blackjack? Type 'y' or 'n'. ")
if answer == 'y':
  game_running = True
  print(logo)
  dealer_hits_soft = int(input("Dealer hits on soft 'x' (enter a number). "))
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  instances_each_card = 4
  deck = cards * instances_each_card
  number_decks = int(input("How many decks would you like to play with? "))
  shoe = (deck * number_decks)
  random.shuffle(shoe)
  cards_in_shoe = len(shoe)
  shuffle_point = float(input("At what point would you like the shoe to be shuffled? (e.g. 75% of cards in the shoe have been dealt, insert as '75') ")) / 100
  card_counter = 0
  while game_running:
    your_cards = []
    dealer_cards = []
    your_cards.append(deal_one_card())  #First card dealt in hand to you
    dealer_cards.append(deal_one_card())  #First card dealt in hand to dealer
    your_cards.append(deal_one_card())  #Second card dealt in hand to you
    dealer_cards.append(deal_one_card())  #Second card dealt in hand to dealer
    your_total = sum(your_cards)
    dealer_total = sum(dealer_cards)
    print(f"Your cards {your_cards}, current_total: {your_total}")
    print(f"Dealer's first card: {dealer_cards[0]}")
    if dealer_total == 21:
      print(f"Dealer has blackjack. {dealer_cards}. Dealer wins. Game over.")
    elif your_total == 21:
      print(f"You have blackjack. {your_cards}. You win. Game over.")
    else:
      hit_or_stand = input("Do you want to hit or stand. Type 'h' or 's'. ")
      if hit_or_stand == 'h':
        your_actions()
      if hit_or_stand == 's':
         dealer_actions()
    percent_of_shoe_used = card_counter / cards_in_shoe
    print(f"Percent of shoe used: {percent_of_shoe_used: .0%}")
    continue_playing = input("Do you want to play again? Type 'y' or 'n'. ")
    if continue_playing == 'y' and percent_of_shoe_used <= shuffle_point:
      os.system('clear')
    elif continue_playing == 'y':
      blinking_ellipses("Dealer shuffling")
      card_counter = 0
      os.system('clear')
      random.shuffle(shoe)
    else:
      print("Ok.  No more blackjack for you.")
      game_running = False
else:
  print("Game over.")
  game_running = False
