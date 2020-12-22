def bintang(n):
    x = n
    for i in range(n-3):
        a = 1+2*i
        print(('*'*a).center(x))
    for a in range(n):
        b = 5-2*a
        print(('*'*b).center(x))
bintang(7)
