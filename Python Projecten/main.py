tweeEuroMunt = 2
eenEuroMunt = 1
vijftigEurocent = 0.5
twintigEurocent = 0.2
tienEurocent = 0.1
vijfEurocent = 0.05
tweeEurocent = 0.02
eenEurocent = 0.01

aantalTweeEuroMunt = 93
aantalEenEuroMunt = 1
aantalVijftigEurocent = 0
aantalTwintigEurocent = 2
aantalTienEurocent = 0
aantalVijfEurocent = 1
aantalTweeEurocent = 0
aantalEenEurocent = 0

bedrag = "Het bedrag is: " + str(round(tweeEuroMunt * aantalTweeEuroMunt + eenEuroMunt * aantalEenEuroMunt + vijftigEurocent * aantalVijftigEurocent + twintigEurocent * aantalTwintigEurocent + tienEurocent * aantalTienEurocent + vijfEurocent * aantalVijfEurocent + tweeEurocent * aantalTweeEurocent + eenEurocent * aantalEenEurocent, 2))
inCenten = "rest in centen is " + str((aantalTienEurocent * tienEurocent + aantalVijfEurocent * vijfEurocent + aantalTweeEurocent * tweeEurocent + aantalEenEurocent * eenEurocent) * 100)

print(bedrag)

print(str(aantalTweeEuroMunt) + " 2-euromunt")
print(str(aantalEenEuroMunt) + " 1-euromunt")
print(str(aantalVijftigEurocent) + " 50-eurocent")
print(str(aantalTwintigEurocent) + " 20-eurocent")

print(inCenten)

print(str(aantalTienEurocent) + " 10-eurocent")
print(str(aantalVijfEurocent) + " 5-eurocent")
print(str(aantalTweeEurocent) + " 2-eurocent")
print(str(aantalEenEurocent) + " 1-eurocent")

