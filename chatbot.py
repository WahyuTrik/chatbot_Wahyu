import re
import random

sapaan = ["halo juga", "hai juga",]

while True:
    
    x = input("user\t: ")
    if re.findall(r'halo|hai', x):
        print("Bot\t:", random.choice(sapaan))
        
    else:
        print("Bot\t: Saya tidak paham")