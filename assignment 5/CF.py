Fred   = [1, 3, 1.5, 3, 1, 3]
Lilian = [3, 1.5, 2, 2, 3, 1]
Cathy  = [2, 2, 2, 3, 1.5, 2]
John   = [3, 2, 2, 2, None, None]

BonJovi = [1,3,2,3]
Metallica = [3,1.5,2,2]
Scorpians = [1.5,2,2,2]
ACDC = [3,2,3,2]
Kiss = [1,3,1.5, None]
Guns = [3,1,2,None]

def cosSimil(user1, user2):
    sumOfProducts = 0
    sumOfSquared1 = 0
    sumOfSquared2 = 0
    for i in range(len(user1)):
        if user1[i] is None or user2[i] is None:
            continue
        sumOfProducts += user1[i] * user2[i]
        sumOfSquared1 += user1[i]**2
        sumOfSquared2 += user2[i]**2
    return sumOfProducts / (sumOfSquared1 * sumOfSquared2) ** (1/2)

c1 = cosSimil(Guns, BonJovi)
c2 = cosSimil(Guns, Metallica)
c3 = cosSimil(Guns, Scorpians)
c4 = cosSimil(Guns, ACDC)

print(c1)
print(c2)
print(c3)
print(c4)
print()

m = (3+1+2)/3
x1 = (3+1.5+2)/3
x2 = (3+2+3)/3

wc = m + (c1*(2-x1) + c3*(2-x2) )/(c2+c4)
print(m)
print(x1)
print(x2)
print(wc)