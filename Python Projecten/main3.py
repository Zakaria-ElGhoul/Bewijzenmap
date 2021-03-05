print("Wat is uw gewicht?")
gewicht = float(input())

print("Wat is uw lengte?")
lengte = float(input())

BMI = gewicht / lengte ** 2

if BMI >= 27:
    print("U bent volgens de BMI-index te zwaar.")
elif BMI >= 25:
    print("U loopt risico op overgewicht.")
elif BMI <= 20:
    print("Je hebt kanker zware anorexia G. Beter ga je chappen amk!!!")
else:
    print("nice cock bro")

print(round(BMI, 2))