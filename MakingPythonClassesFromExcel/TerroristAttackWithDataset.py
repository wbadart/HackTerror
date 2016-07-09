import csv
import TerroristAttack
import pickle

with open("globalterrorismdb_0616dist.csv", "r") as ins:
    firstLine = True
    array = []
    terroristAttacks = []
    for line in ins:
        if firstLine:
            firstLine = False
            continue
        else:
            array.append(line)
    for line in array:
        t = TerroristAttack.TerroristAttack(line)
        terroristAttacks.append(t)


for terroristAttack in terroristAttacks:
    print(terroristAttack.eventid,end=" ")
    print(terroristAttack.city,end=", ")
    print(terroristAttack.country_txt, end=" (")
    print(terroristAttack.latitude, end = ", ")
    print(terroristAttack.longitude, end=") ")
    print()



