print("Wat is het gewicht van uw bagage?")
gewicht = int(input())

if gewicht > 20:
    print("Er moet een toeslag van 25,- euro betaald worden voor bagage die te zwaar is.")
elif gewicht == 20:
    print("Poeh! Dat gewicht is precies goed")
else:
    print("Goede reis!")