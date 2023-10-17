# factoriaal recursie

def fact(getal):
    if(getal <= 1):
        return 1
    return getal * fact(getal - 1)

print(fact(999))