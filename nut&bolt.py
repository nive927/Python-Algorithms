def matchingNutsBolts(nuts, bolts):
    for i in range(0, len(nuts)):
        for j in range(i, len(bolts)):
            if(nuts[i] == bolts[j]):
                bolts[i], bolts[j] = bolts[j], bolts[i]
                
    print("After matching: ")
    print(bolts)

#Driver 

nuts = ['!', '@', '#', '$', '%', '^']
bolts = ['^', '%', '$', '#', '@', '!']

print("Nuts: ", nuts)
print("Bolts: ", bolts)
         
matchingNutsBolts(nuts, bolts)
print("Nuts")
print(nuts)