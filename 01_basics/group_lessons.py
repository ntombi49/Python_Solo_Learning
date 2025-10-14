# Have our names in a list....dimpho, ntombi, bosslady, Nokx, Liya
# I found the culprit when you reach bosslady

names = ['Dimpho', 'Ntombi', 'BossLady', 'Nokx', 'Liya']
for n in names:
    if n == "BossLady":
        print("I found the culprit")
        
# random.shuffle
# Have my name as a string = Ntombi
# Itterate through letters of my name and print randomly
import random
name = list("Ntombi")
print(name)
random.shuffle(name)
for letter in name:
    print(letter)



