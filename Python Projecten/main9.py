import random

i = 0
# def = functie
def schudKaarten():

    #list van alle strings
    speelKaart = ["Harten", "Schoppen", "Klaveren", "Ruiten"]
    waardes = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Boer", "Dishwasher", "Heer", "Aas"]

    #hier maak ik een random integer aan, lists geven elke keer een error als ik de lengte wil
    randSpeelkaart = random.randint(0, 3)
    ranWaardes = random.randint(0, 12)

    #hier print hij de kaarten uit
    randomKaarten = print(str(speelKaart[randSpeelkaart]) + " " + str(waardes[ranWaardes]))

#wannneer de while loop aan is, blijft de applicatie runnen
while i < 5:

    print("Typ schud om te schudden")
    #text wordt naar lowercase gezet voor als het hoofdletter gevoelig is
    invoerText = input().lower()

    if invoerText == "schud":
    #hier print hij alles uit 
        for j in range(0,6):
            schudKaarten()
    else:
        print("U heeft het verkeerd getypt!")
    i += 1