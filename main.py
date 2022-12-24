
import random

print("----------------")
print("GUESS THE NUMBER")
print("----------------")
print("   ")
print("Select a level!")
print("   ")
print("e for easy, m for medium and h for hard. Then press enter!")
print("   ")
level = input("Level:   ")
print("   ")
if level == "e":
  number = random.randint(1, 25)
  print("My number is between 1 and 25")
  answer = input("Enter your number here:  ")
  while answer != number:
    answer = input("Enter your number here, the previous answer is wrong:  ")
    if int(answer) > int(number):
      print("That is too high, try again!")
    elif int(answer) < int(number):
      print("That is too low, try again!")
    else:
      print("YES! That is the number!")
      break
elif level == "m":
  number = random.randint(1, 50)
  print("My number is between 1 and 50")
  answer = input("Enter your number here:  ")
  while answer != number:
    answer = input("Enter your number here, the previous answer is wrong:  ")
    if int(answer) > int(number):
      print("That is too high, try again!")
    elif int(answer) < int(number):
      print("That is too low, try again!")
    else:
      print("YES! That is the number!")
      break
elif level == "h":
  number = random.randint(1, 100)
  print("My number is between 1 and 100")
  answer = input("Enter your number here:  ")
  while answer != number:
    answer = input("Enter your number here, the previous answer is wrong:  ")
    if int(answer) > int(number):
      print("That is too high, try again!")
    elif int(answer) < int(number):
      print("That is too low, try again!")
    else:
      print("YES! That is the number!")
      break
else:
  print("That is not a level.")
    


