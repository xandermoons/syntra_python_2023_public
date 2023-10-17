with open("02_Python_Basis/files/hello.txt", mode="r", encoding='utf-8') as my_file:
    print(my_file.read())

print()

with open("02_Python_Basis/files/hello.txt", mode="a", encoding='utf-8') as my_file:
    nieuwe_lijn = '\n' + input('Geef een nieuwe lijn in: ')
    my_file.write(nieuwe_lijn)


