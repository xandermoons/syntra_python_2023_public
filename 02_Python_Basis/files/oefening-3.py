producten = list()

def read_product_file():
    with open('02_Python_Basis/files/producten.txt', mode='r') as f:
        for line in f.readlines():
            pro,pri = line.split(',')
            pri = pri.strip()
            producten.append([pro,pri])

def add_product():
    pro = input('Geef de naam van het product: ')
    pri = input('Geef de prijs van het product: ')
    producten.append([pro,pri])

def change_product():
    pro = input('Geef de naam van het product dat u wil wijzigen: ')
    n_pro = input('Geef de nieuwe naam: ')

    for product in producten:
        if product[0] == pro:
            product[0] = n_pro

def change_price():
    pro = input('Geef de naam van het product waarvan u de prijs wil wijzigen: ')
    n_pri = input('Geef de nieuwe prijs: ')

    for product in producten:
        if product[0] == pro:
            product[1] = n_pri

def write_products():
    with open('02_Python_Basis/files/producten.txt', mode='w') as f:
        f.writelines([f"{product[0]},{product[1]}\n" for product in producten])

def main ():
    read_product_file()
    print(producten)
    # change_price()
    # write_products()

main()

