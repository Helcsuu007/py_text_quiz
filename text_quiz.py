# Storing the correct answers.
correct = 0 

# Prompting the player's name and starting the game.
name = input ("What's your name? ")

print(f"\nHello {name}, let's get started, shall we?"
    " To answer write 'true' or 'false'.")

# Questions and t/f loops.
print(f"\nThe capital city of Hungary is Bukarest.")

answer = input(">>> ")
if answer == "false":
    correct += 1
else:
    correct += 0


print(f"\nApple launched the first iPhone in 2005.")

answer = input(">>> ")
if answer == "false":
    correct += 1
else:
    correct += 0


print(f"\nThe first president of the United States was George Washington.")

answer = input(">>> ")
if answer == "true":
    correct += 1
else:
    correct += 0


print(f"\nChristopher Nolan directed the 2014 sci-fi 'Interstellar'.")

answer = input(">>> ")
if answer == "true":
    correct += 1
else:
    correct += 0


print(f"\nNetflix, Inc. was founded in 2007.")

answer = input(">>> ")
if answer == "false":
    correct += 1
else:
    correct += 0


print(f"\nThe symbol for potassium is 'K'.")

answer = input(">>> ")
if answer == "true":
    correct += 1
else:
    correct += 0


# Evaluating the player's performance in the quiz.
print(f"\nThanks for playing, {name}. Correct answers: {correct}/6.")
