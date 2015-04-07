mass = [i for i in range(0,10)]
z=0
i = 0
while True:
    mass[i] = 0
    i+=1
    if i == 10:
        break
i=0
x=1
print('start')

def test():
    i = 0
    if mass[i] < 2:
        mass[i]+=1
    else:
        while True:
            mass[i] =0
            i+=1
            if mass[i] < 2:
                mass[i]+=1
                break
    print(mass)
              
flag = True
while flag:
    q=0
    test()
    for w in mass:
        q+=w
        if q ==20:
            flag = False
            break
    
