#rock/paper/scissors

player1_score = 0
player2_score = 0

options = ['paper', 'rock', 'scissors']

while player1_score != 3 and player2_score != 3:
  player_choice_is_correct = True

  while player_choice_is_correct:
    player1_choice = input('Player 1 - give your choice: ')
    if player1_choice in options:
      player_choice_is_correct = False

  player_choice_is_correct = True

  while player_choice_is_correct:
    player2_choice = input('Player 2 - give your choice: ')
    if player2_choice in options:
      player_choice_is_correct = False

  if player1_choice == 'paper' and player2_choice == 'rock' \
          or player1_choice == 'rockn' and player2_choice == 'scissors' \
          or player1_choice == 'scissors' and player2_choice == 'papier':
    print('Player 1 won !')
    player1_score += 1
  elif player1_choice == player2_choice:
    print('A draw')
  else:
    print('Player 2 won !')
    player2_score += 1

from time import sleep

for pojemnik in  [5, 4, 3, 2, 1]:
  print (pojemnik)
  sleep(1)
  if pojemnik <= 3:
    sleep(2)

if player1_score > player2_score:
  print('Congratulation Player 1 !!!')
else:
  print('Congratulation Player 2 !!!')