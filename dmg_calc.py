import random
import sys
from traceback import print_tb
from xml.etree.ElementTree import fromstringlist

super_e = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #none
[0,0,0,0,0,0,0,1,0,0,0,1,1,0,0], #Bug
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Dragon
[0,0,0,0,0,1,0,0,0,0,0,0,0,0,1], #Electric
[0,0,0,0,0,0,0,0,0,1,1,0,0,1,0], #Fighting
[1,0,0,0,0,0,0,1,0,1,0,0,0,0,0],#Fire
[1,0,0,1,0,0,0,1,0,0,0,0,0,0,0],#Flying
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Ghost
[0,0,0,0,0,0,0,0,1,0,0,0,0,1,1],#Grass
[0,0,1,0,1,0,0,0,0,0,0,1,0,1,0],#Ground
[0,1,0,0,0,1,0,1,1,0,0,0,0,0,0],#Ice
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Normal
[1,0,0,0,0,0,0,1,0,0,0,0,0,0,0],#Poison
[0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],#psychic
[1,0,0,0,1,1,0,0,0,1,0,0,0,0,0],#rock
[0,0,0,0,1,0,0,0,1,0,0,0,0,1,0],#water
]
not_s_e = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #none
[0,0,0,0,1,1,0,0,0,0,0,0,0,1,0], #Bug
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Dragon
[0,0,1,0,0,0,0,1,0,0,0,0,0,0,0], #Electric
[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0], #Fighting
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1], #Fire
[0,0,1,0,0,0,0,0,0,0,0,0,0,1,0], #Flying
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Ghost
[1,0,0,0,1,1,0,1,0,0,0,1,0,0,0], #Grass
[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0], #Ground
[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1], #Ice
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Normal
[0,0,0,0,0,0,0,0,1,0,0,0,0,1,0], #Poison
[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0], #Psychic
[0,0,0,1,0,0,0,0,0,0,0,0,0,1,0], #Rock
[0,0,0,0,0,0,0,1,0,1,0,0,0,0,0], #Water 
]
no_e = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#none
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Bug
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Dragon
[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0], #Electric
[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0], #Fighting
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Fire
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Flying
[0,0,0,0,0,0,0,0,0,0,1,0,1,0,0], #Ghost
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Grass
[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0], #Ground
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Ice
[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0], #Normal
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Poison
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Psychic
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Rock
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Water 
]

Sunny = [
[0],
[0], #Bug
[0], #Dragon
[0], #Electric
[0], #Fighting
[1], #Fire
[0], #Flying
[0], #Ghost
[0], #Grass
[0], #Ground
[0], #Ice
[0], #Normal
[0], #Poison
[0], #Psychic
[0], #Rock
[2], #Water
]
Fog  = [
[0],
[0], #Bug
[0], #Dragon
[2], #Electric
[0], #Fighting
[0], #Fire
[0], #Flying
[0], #Ghost
[0], #Grass
[0], #Ground
[0], #Ice
[0], #Normal
[0], #Poison
[0], #Psychic
[0],#Rock
[0],#Water
]

Snow = [
[0],
[0], #Bug
[0], #Dragon
[0], #Electric
[0], #Fighting
[0], #Fire
[0], #Flying
[0], #Ghost
[0], #Grass
[0], #Ground
[1], #Ice
[0], #Normal
[0], #Poison
[0], #Psychic
[0], #Rock
[0], #Water
]
Rain  = [
[0],
[0], #Bug
[0], #Dragon
[0], #Electric
[0], #Fighting
[2], #Fire
[0], #Flying
[0], #Ghost
[0], #Grass
[0], #Ground
[0], #Ice
[0], #Normal
[0], #Poison
[0], #Psychic
[0], #Rock
[1], #Water
]
Hail = [
[0],
[2], #Bug
[2], #Dragon
[2], #Electric
[2], #Fighting
[2], #Fire
[2],#Flying
[2], #Ghost
[2], #Grass
[2], #Ground
[1], #Ice
[2], #Normal
[2],#Poison
[2],#Psychic
[2], #Rock
[2], #Water
]
Sandstorm  = [
[0],
[2], #Bug
[2], #Dragon
[2], #Electric
[2], #Fighting
[2], #Fire
[2], #Flying
[2], #Ghost
[2], #Grass
[0], #Ground
[2], #Ice
[2], #Normal
[2], #Poison
[2], #Psychic
[1], #Rock
[2], #Water
]
Cloudy  = [
[2], #Bug
[2], #Dragon
[2], #Electric
[2], #Fighting
[2], #Fire
[2], #Flying
[2], #Ghost
[2], #Grass
[2], #Ground
[2], #Ice
[0], #Normal
[2], #Poison
[2], #Psychic
[2], #Rock
[2], #Water
]

Stab = [
[1], #Bug
[2], #Dragon
[3], #Electric
[4], #Fighting
[5], #Fire
[6], #Flying
[7], #Ghost
[8],#Grass
[9],#Ground
[10], #Ice
[11], #Normal
[12], #Poison
[13], #Psychic
[14],#Rock
[15], #Water
]


print("Pokemon Damage Calculator")
level = int(input("Level: "))
A = int(input("A: "))
D = int(input("D: "))
Power = int(input("Power: "))
num_type = input("""Select type of your pokemon:
[1] Bug
[2] Dragon
[3] Electric
[4] Fighting
[5] Fire
[6] Flying
[7] Ghost
[8] Grass
[9] Ground
[10] Ice
[11] Normal
[12] Poison
[13] Psychic
[14] Rock
[15] Water
opt: """)
if int(num_type) == 1:
    type = "Bug"
elif int(num_type) == 2:
    type = "Dragon"
elif int(num_type) == 3:
    type = "Electric"
elif int(num_type) == 4:
    type = "Fighting"
elif int(num_type) == 5:
    type = "Fire"
elif int(num_type) == 6:
    type = "Flying"
elif int(num_type) == 7:
    type = "Ghost"
elif int(num_type) == 8:
    type = "Grass"
elif int(num_type) == 9:
    type = "Ground"
elif int(num_type) == 10:
    type = "Ice"
elif int(num_type) == 11:
    type = "Normal"
elif int(num_type) == 12:
    type = "Poison"
elif int(num_type) == 13:
    type = "Psychic"
elif int(num_type) == 14:
    type = "Rock"
elif int(num_type) == 15:
    type = "Water"
else: 
    type = "type doesn't exist"

print("You selected: " + type)

#oppenent 
o_num_type = input("""Select type of opponent:
[1] Bug
[2] Dragon
[3] Electric
[4] Fighting
[5] Fire
[6] Flying
[7] Ghost
[8] Grass
[9] Ground
[10] Ice
[11] Normal
[12] Poison
[13] Psychic
[14] Rock
[15] Water
opt: """)
if int(o_num_type) == 1:
    o_type = "Bug"
elif int(o_num_type) == 2:
    o_type = "Dragon"
elif int(o_num_type) == 3:
    o_type = "Electric"
elif int(o_num_type) == 4:
    o_type = "Fighting"
elif int(o_num_type) == 5:
    o_type = "Fire"
elif int(o_num_type) == 6:
    o_type = "Flying"
elif int(o_num_type) == 7:
    o_type = "Ghost"
elif int(o_num_type) == 8:
    o_type = "Grass"
elif int(o_num_type) == 9:
    o_type = "Ground"
elif int(o_num_type) == 10:
    o_type = "Ice"
elif int(o_num_type) == 11:
    o_type = "Normal"
elif int(o_num_type) == 12:
    o_type = "Poison"
elif int(o_num_type) == 13:
    o_type = "Psychic"
elif int(o_num_type) == 14:
    o_type = "Rock"
elif int(o_num_type) == 15:
    o_type = "Water"
else: 
    o_type = "type doesn't exist"
    sys.exit()
print("You selected: " + o_type)


#SE/NVE/ND
if super_e[int(num_type)][int(o_num_type)-1] == 1:
    e_type = random.choice([2, 4])
    print("Super Effective")
elif not_s_e[int(num_type)][int(o_num_type)-1] == 1:
    e_type = random.choice([0.25, 0.5])
    print("Not Very effective")
elif no_e[int(num_type)][int(o_num_type)-1] == 1:
    e_type = 0
    print("No Effect")
else: 
    e_type = 1 
    print("Normal Damage")


Target = int(input("How Many Target?: "))

#Weather

wthr = input("""
[1] Sunny
[2] Fog
[3] Rain
[4] Hail
[5] Sandstorm
[6] Cloudy
[7] Normal
opt: """)


if int(wthr) == 1:
    if Sunny[int(num_type)][0] == 1:
        weather = 1.5
    elif Sunny[int(num_type)][0] == 2:
        weather = 0.5
    elif Sunny[int(num_type)][0] == 0: 
        weather = 1
elif int(wthr) == 2:
    if Fog[int(num_type)][0] == 1:
        weather = 1.5
    elif Fog[int(num_type)][0] == 2:
        weather = 0.5
    elif Fog[int(num_type)][0] == 0: 
        weather = 1
elif int(wthr) == 3:
    if  Rain[int(num_type)][0] == 1:
        weather = 1.5
    elif Rain[int(num_type)][0] == 2:
        weather = 0.5
    elif Rain[int(num_type)][0] == 0: 
        weather = 1
elif int(wthr) == 4:
    if Hail[int(num_type)][0] == 1:
        weather = 1.5
    elif Hail[int(num_type)][0] == 2:
        weather = 0.5
    elif Hail[int(num_type)][0] == 0:
        weather = 1
elif int(wthr) == 5:
    if Sandstorm[int(num_type)][0] == 1:
        weather = 1.5
    elif Sandstorm[int(num_type)][0] == 2:
        weather = 0.5
    elif Sandstorm[int(num_type)][0] == 0: 
        weather = 1
elif int(wthr) == 6: 
    if Cloudy[int(num_type)][0] == 1:
        weather = 1.5
    elif Cloudy[int(num_type)][0] == 2:
        weather = 0.5
    elif Cloudy[int(num_type)][0] == 0: 
        weather = 1
elif int(wthr) == 7:
    weather = 1 
#Badges
if (int(num_type)) == 14:    
    ans = input("Do you have Boulder Badge? (y/n) :")    
    if ans.lower() == "y":
        badge = 1.25
    else: badge = 1
elif (int(num_type)) == 15:
    ans = input("Do you have Cascade Badge? (y/n) :")
    if ans.lower() == "y":
        badge = 1.25
    else: badge = 1
elif (int(num_type)) == 3:
    ans = input("Do you have Thunder Badge? (y/n) :")
    if ans.lower() == "y":
        badge = 1.25
    else: badge = 1
elif (int(num_type)) == 8:
    ans = input("Do you have Rainbow Badge? (y/n) :")
    if ans.lower() == "y":
        badge = 1.25
    else: badge = 1
elif (int(num_type)) == 12:
    ans = input("Do you have Soul Badge? (y/n) :")
    if ans.lower() == "y":
        badge = 1.25
    else: badge = 1
elif (int(num_type)) == 13:
    ans = input("Do you have Marsh Badge? (y/n) :")
    if ans.lower() == "y":
        badge = 1.25
    else: badge = 1
elif (int(num_type)) == 5:
    ans = input("Do you have Volcano Badge? (y/n) :")
    if ans.lower() == "y":
        badge = 1.25
    else: badge = 1
elif (int(num_type)) == 9:
    ans = input("Do you have Earth Badge? (y/n) :")
    if ans.lower() == "y":
        badge = 1.25
    else: badge = 1
else: badge = 1

crit = random.randint(1,2)
print(crit)
ran = random.uniform(.85, 1)
print(ran)

num_atk_type = input("""Enter Attack type: 
[1] Bug
[2] Dragon
[3] Electric
[4] Fighting
[5] Fire
[6] Flying
[7] Ghost
[8] Grass
[9] Ground
[10] Ice
[11] Normal
[12] Poison
[13] Psychic
[14] Rock
[15] Water
opt:
""")
if int(num_type) == int(num_atk_type):
    STAB = 1.5
else: STAB = 1

burn = input("is the attacker is burned? (y/n) :")
if burn.lower() == "y":
    burn_type = 0.5
else: burn_type = 1

other = 1 

Modifier = (Target * weather * badge * crit * ran * STAB * e_type* burn_type * other)

damage = ((((((2*level)/5)+2)* Power * (A/D))/50 ) + 2) * Modifier

print(f"""
Modifier: {Modifier}
ran: {ran}
Critical: {crit}
STAB: {STAB}
Effective Damage: {e_type}
Damage: {damage}""")
