import random


userRandAmmount = int(input("Enter how many numbers you want to guess: "))
RandomNumber = random.randint(1, userRandAmmount)
userChances = int(input("Enter the ammount of chances you want: "))
counter = 0

print("Guess the random number, you have " + str(userChances) + " chances!")

while counter < userChances:
  userNumber = int(input("Enter number: "))
  if userNumber == RandomNumber:
    print("You guessed the Number!")
    break
  elif userNumber < RandomNumber:
    print("Higher")
  elif userNumber > RandomNumber:
    print("lower")
  counter += 1 
  print("You have " + str(userChances - counter) + " chances left.")


  