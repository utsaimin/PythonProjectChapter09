import random
def shuffleString(x, n):
    listHasil = []
    i = 0
    while i < n :
        acak = ' '.join(random.sample(x, len(x)))
        if(acak not in listHasil):
            listHasil += [acak]
            i +=1
    print(listHasil)

shuffleString('aku', 6)
