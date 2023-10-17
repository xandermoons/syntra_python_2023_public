names = list()

with open("02_Python_Basis/files/namen.txt", mode="r") as f:
    for line in f.readlines():
        name = line.strip()
        names.append(name)

print(names)

def add_name():
    name = input("Geef de nieuwe naam in: ")
    names.append(name)

def delete_name():
    name = input('Geef de naam in die u wilt verwijderen: ')
    if name in names:
        names.remove(name)

def write_names():
    with open("02_Python_Basis/files/namen.txt", mode="w") as f:
        f.writelines([f"{name}\n" for name in names])

def main():
    add_name()
    add_name()
    delete_name()
    write_names()

main()