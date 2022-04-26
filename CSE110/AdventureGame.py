print()
print("A brave adventurer walks into a tavern called the Green Dragon Inn and you see a man holiding two weapons and he asks you a question." )
print()
weapon = input("You must be the person Gandolf told me about, it is great to meet you I am Tom Bombadil. We have no time to waste, what weapon do you choose SWORD or BOW?  ")
print()
if weapon.lower() == "sword":
    print("That means you are from the house of Gondor!" )
elif weapon.lower() == "bow":
    print("That means you are from the house of Rivendell!" )
else:
    print("That means you must be from the SHIRE!" )
print()
print("You pick up your weapon and are memorized by how it is crafted. You look at Tom and say where do I head next? ")
print()
location = input("You have three options adventurer you can go help Frodo with the RING, help ROHAN at Edoras, or fight giant spiders at the FOREST of Mirkwood? ")
print()
if location.lower() == "ring":
    print("You must head to Rivendell and meet with the fellowship, go now adventurer. ")
elif location.lower() == "rohan":
    print("You must head to Edoras and meet with King Theoden, go now adventurer. ")
elif location.lower() == "forest":
    print("You must head to mirkwood and meet with King Thranduil, go now adventurer. ")
else:
    print("If you don't like the three locations I have given you, then you must go to Mordor and fight all the orcs by yourself." )
print()
print("You run to the door leading out of the tavern and you hear a loud voice out of the corner say adventurer! You turn around to find a giant man who carries a battle axe. You look at this tall figure and say how may I help you? ")
print()
choice = input("He looks down on you and says, I over heard your conversation and I know Gandolf as well. He asks with a stern voice may I join you on your quest. You look at him and say 'YES or NO' ")
print()
if choice.lower() == "yes":
    print("You say come on we don't have much time! ")
elif choice.lower() == "no":
    print("I am sorry but you will just slow me down with that big battle axe. ")
else:
    print("The Giant looks at you and says its a yes or no question, never mind I will stay here and drink because you are weird anyway." )
print()
print("Then you open the door and head on to your adventure. ")
print()
food = input("You head outside and see a man selling a pig and a chicken. 'You are very hungry.' The man looks at you, and says you look hungry would you like to have one of these animals? What do you choose a 'PIG or the CHICKEN' ")
print()
if food.lower() == "pig":
    print("You have picked a great choice, you will have a ton of rations but it will slow you down. ")
elif food.lower() == "chicken":
    print("You have made a great choice but you will not have a lot of rations but will get you your destination faster." )
else:
    print("Oh that is a weird choice but okay I will take the pig and the chicken to the Shire to sell them." )
print()
print("Then you jump on your trusty stallion Shadowfax and ride into the dark night." )
print()