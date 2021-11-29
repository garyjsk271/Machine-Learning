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

def cos(user1, user2):
    sumOfProducts = 0.0
    sumOfSquared1 = 0.0
    sumOfSquared2 = 0.0
    for i in range(len(user1)):
        if user1[i] is None or user2[i] is None:
            continue
        sumOfProducts += user1[i] * user2[i]
        sumOfSquared1 += user1[i]**2
        sumOfSquared2 += user2[i]**2
    return sumOfProducts / ((sumOfSquared1 * sumOfSquared2) ** (1/2))
def mean(array):
    sum = 0
    count = 0
    for value in array:
        if value:
            sum += value
            count += 1
    return sum/count
c1 = cos(Guns, BonJovi)
c2 = cos(Guns, Metallica)
c3 = cos(Guns, Scorpians)
c4 = cos(Guns, ACDC)

print(c1)
print(c2)
print(c3)
print(c4)
print()

m = mean(Guns[:3])
m1 = mean(Metallica[:3])
m2 = mean(ACDC[:3])
c1, c2 = c2, c4
print(c1, c2)
wc = m + (c1*(2-m1) + c2*(2-m2) )/(c1+c2)

print(m)
print(m1)
print(m2)
print(wc)