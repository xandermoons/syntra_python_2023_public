n = input('Geef een positief geheel getal (max 20): ')
n = int(n)


def fibo(n):
    fibo_lijst = []
    i = 0
    eerste = 0
    tweede = 1
    fibo_lijst.append(eerste)
    fibo_lijst.append(tweede)
    while i < n:
        derde = eerste + tweede
        fibo_lijst.append(derde)
        eerste = tweede
        tweede = derde
        i += 1
    return fibo_lijst[:n]

print(fibo(n))
