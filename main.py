from art import logo, vs
from game_data import data
import random


#the following functions take a dictionary as a parameter and returns the value from each key
def get_name(dictionary):
  name = dictionary["name"]
  return name

def get_description(dictionary):
  description = dictionary["description"] 
  return description

def get_country(dictionary):
  country = dictionary["country"] 
  return country
def get_follower_count(dictionary):
  follower_count = dictionary["follower_count"]
  return follower_count

#interface function takes on choice's A and B as parameters. Prints the values from each key and the "vs" ASCII art
def interface(choice_A, choice_B):
  print(f"{get_name(choice_A)} is a {get_description(choice_A)} from {get_country(choice_A)}")
  print(vs)
  print(f"{get_name(choice_B)} is a {get_description(choice_B)} from {get_country(choice_B)}")
  
#scoring_calculation takes on choice's A and B as parameters. Checks of either of them are correct and returns a boolean of True or False
def scoring_calculation(choice_A, choice_B):
  valid_inputs = ['a', 'b']
  
  interface(choice_A, choice_B)
  print("Who has the most Instagram followers? ")
  user_pick = input(f"Choose 'A' for {get_name(choice_A)} or choose 'B' for {get_name(choice_B)}: ").lower()
  choice_A_followers = get_follower_count(choice_A)
  choice_B_followers = get_follower_count(choice_B)
  while user_pick not in valid_inputs:
    user_pick = input("Invalid selection please select either 'A' or 'B': ")
    
  if user_pick == "a" and choice_A_followers > choice_B_followers:
    
    print("You win this round!")
    return True
  elif user_pick == "b" and choice_B_followers > choice_A_followers:
    
    print("You win this round!")
    return True
  else:
    print("Aww, you lose!")
    return False
  
#The high or low game
should_continue = True
print(logo)
final_score = 0
#check if there is enough data to play the game
if len(data) < 2:
    print("Insufficient data. The game cannot be played.")
    should_continue = False
#while loop that continues to play the game if should_continue is True and increments the final_score varibale. 
while should_continue: 
  choice_A = random.choice(data)
  choice_B = random.choice(data)
  while choice_A == choice_B:
    choice_B = random.choice(data)
  if scoring_calculation(choice_A,choice_B) == False:
    should_continue = False
  else:
    final_score += 1
     
print(f"Your final score is: {final_score}") 


  
  
