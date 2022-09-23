import random

list1 = ["Yell at ", "Lick ", "Run at ", "Jump On ", "Make fun of ", "kick ","sniffe "]
list2 = ["Your sibling ", "Car ", "Your butt ", "poop ", "a worm ", "a tree ","a dog "]
list3 = ["your crush ", "your mom ", "the US president ", "the worst person in the world "]
dare = "I dare you to " +  random.choice(list1) + "" + random.choice(list2) + "in front of " + random.choice(list3)

print(dare)