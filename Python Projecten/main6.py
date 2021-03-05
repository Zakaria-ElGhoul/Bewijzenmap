#rente is gwn gemmidelde bij abn volgensmij >:)
rentePercentage = 2.5 / 100

def berekenSaldo():
    
    eindbedrag = beginBedrag * loopTijd * rentePercentage

    return beginBedrag + eindbedrag

print("Wat is uw begin bedrag:")
beginBedrag = float(input())
print("Tot hoeveel jaar wilt uw dat wij het berekenen:")
loopTijd = int(input())

print("Over", loopTijd, "jaar heeft u:", berekenSaldo())