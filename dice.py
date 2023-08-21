import random
rolls=int(input("Mention the number of the rolls"))
while rolls:   
    print(random.randint(1,6))
    rolls -= 1