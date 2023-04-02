from functions import randomizer;
print("Hello, welcome to the number guesser game");
d= randomizer()
Number = d.randomNum();
print(Number);

guessed = False;
while guessed == False:
    guess = int(input("guess a number between 0 and 4"))
    if guess == Number:
        print("You got it")
        guessed = True;
    else:
        print("not it")

print("YAYIE")

