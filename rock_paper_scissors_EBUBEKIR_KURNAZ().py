# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 12:47:16 2024

@author: asus
"""

import random

print("INTRODUCTİON TO GAME :Rock, paper, scissors\n it is played by selecting one of the options (rock or paper or scissors) and PC selects one of them, too.\nAccording the rules of the game,\n Rock breaks scissors,\n Scissors cuts paper and\n Paper covers rock.\nWho gets more points wins the game.\nLet's play!")

def rock_paper_scissors_EBUBEKIR_KURNAZ():
    
    game = ["rock", "paper", "scissors"]

    my_points = 0
    pc_points = 0

    while my_points < 2 and pc_points < 2:

        i = random.randint(0,2)
        pc = game[i] 
        choose = input("\nSelect: rock or paper or scissors ? ").lower()
  
        if choose not in game:
          print("Please type your option correctly!")
          continue


        if choose == "rock":
          if pc == "scissors":
            my_points += 1
          elif pc == "paper":
            pc_points += 1
        elif choose == "paper":
          if pc == "rock":
            my_points += 1
          elif pc == "scissors":
            pc_points += 1
        else:
          if pc == "rock":
            pc_points += 1
          elif pc == "paper":
            my_points += 1
            
        print("\nYou selected ",choose)
        print("PC selected ",pc)
        print("\nYou got ",my_points," points")
        print("PC got ",pc_points," points")
  
    if my_points > pc_points:
      print("\nYOU WİN!, Congratulations.")
    elif my_points == pc_points:
      print("\nThis time, there is not a winner!")
    else:
      print("\nI WİN!, Next time try again.")
     
    play_again = input("\nWould you like to play the game again? ").lower()
    responses = ["yes","no"]
    pc_answer = random.choice(responses)
    if play_again == "yes" and pc_answer == "yes":
        print("I want to play again, too. Let's play!")
        rock_paper_scissors_EBUBEKIR_KURNAZ()
    else:
        print("Thanks for the game.")
        
      
rock_paper_scissors_EBUBEKIR_KURNAZ()      
    
    