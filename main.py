rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this
game_images =[rock,paper,scissors]
import random
user_s =int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_s >=3 or user_s <0:
  print("you type invalid no. you lose.")
else:  
 print(game_images[user_s])
 computer_s= random.randint(0,2)
 print("computer choose")
 print(game_images[computer_s])

# print(f"computer choose {computer_s}")
 if user_s==0 and computer_s ==2:
  print("You wins!")
 elif user_s ==2 and computer_s ==0:
  print("you lose!")

 elif computer_s > user_s:
  print("You lose")
 elif user_s > computer_s:
  print("you win!")
 elif computer_s==user_s:
  print("its draw mc!")
   

  

