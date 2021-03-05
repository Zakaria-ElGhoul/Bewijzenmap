flesjesNum = 11
flesjes = "flesjes"

for x in range(1, flesjesNum + 1):
    flesjesNum -= 1
    flesjesMin = flesjesNum - 1

    if flesjesMin <= 0:
        flesjesMin = 0;
        flesjes = "flesjes"
        
    if flesjesNum == 1:
        flesjes = "fles"
    else:
        flesjes = "flesjes"

    print(flesjesNum, flesjes ,"met bier op de muur,", flesjesNum , flesjes, "met bier. Open er een, drink hem meteen," ,flesjesMin,)
    print(flesjes, "met bier op de muur.")
