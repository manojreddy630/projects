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
gem=[rock,paper,scissors]
meb=["rock","paper","scissors"]
ui=int(input("enter 1.Rock 2.Paper 3.Scissors : "))
uip=ui-1
print(meb[uip])
print(gem[uip])
import random
ran=random.randint(0,2)
print(meb[ran])
print(gem[ran])

if uip==0 and ran==2 or uip==1 and ran==0 or uip==2 and ran==1:
  print("you win!")
elif uip==0 and ran==0 or uip==1 and ran==1 or uip==2 and ran==2:
  print("Draw")
else:
  print("you loose")     


