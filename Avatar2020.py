name= "Mai"
tries= 1

user1= input("Hello, What is your username? ")
print("Hello", user1 + ".",)
print("Name a charatcer from the Fire Nation: [Hint: They can't fire bend] ")
guess = input("Have a guess: ")
if guess != name:
    print("Nope!! [Hint: Think of a month]")
if guess == name:
    print("There really is mo fathoming the depths of my hatred for this place -Mai [CORRECT!!]")
    exit()
while guess != name:
    tries += 1
    guess= input("Try again: ")
    if guess != name:
        print("Nope... go rewatch Avatar!")
    if guess == name:
        print("Finally! There really is no fathoming the depths of my hatred for this place -Mai [CORRECT!!]")