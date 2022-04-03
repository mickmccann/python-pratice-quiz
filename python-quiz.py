# Python practice

print("Welcome to the Ultimate Stephen King Quiz!")

play = input("Type 'Yes' if you want to test yourself :) ")

if play.lower() != "yes":
    print("Ok! Bye!")
    quit()
else:
    print("Ok, let's play!")

points = 0

# Question 1
question = input("What was the name of Stephen King's first published novel? ")
if question.lower() == "carrie":
    print("CORRECT!")
    points += 1
else:
    print("Incorrect answer.")

# Question 2
question = input("What is the name of the clown that features in the novel IT? ")
if question.lower() == "pennywise":
    print("CORRECT!")
    points += 1
else:
    print("Incorrect answer.")

# Question 3
question = input("What type of dog is Cujo? ")
if question.lower() == "st. bernard" or "st bernard" or "saint bernard":
    print("CORRECT!")
    points += 1
else:
    print("Incorrect answer.")

# Question 4
question = input("In which US state was King born? ")
if question.lower() == "maine":
    print("CORRECT!")
    points += 1
else:
    print("Incorrect answer.")

# Question 5
question = input("How many books has Stephen King published? ")
if question == 64:
    print("CORRECT!")
    points += 1
else:
    print("Incorrect answer.")

# Question 6
question = input("Who played the evil clown in the TV mini series of IT (1990)? ")
if question.lower() == "Tim Curry":
    print("CORRECT!")
    points += 1
else:
    print("Incorrect answer.")

# Question 7
question = input("In which establishment is The Shining set? ")
if question.lower() == "Hotel" or "A hotel":
    print("CORRECT!")
    points += 1
else:
    print("Incorrect answer.")

# Points tally + win precentage
print("Thank you for playing, you got " + str(points) + " correct!")
print("You got " + str((points / 7) * 100) + "%")
