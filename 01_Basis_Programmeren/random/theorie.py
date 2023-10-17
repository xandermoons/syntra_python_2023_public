import random as rd

# random getal tussen 1 en 10
print(f'random getal 1 - 10: {rd.randint(1,10)}') 

# seed zet het kiezen van de random waarde vast. Wordt gebruikt bij shuffle van 
# lijsten zodat ge op dezelfde uitkomsten kunt testen
rd.seed(101)
print(f'seed: {rd.randint(0,10)}')

# getal tussen 0 en 1
print(f'random getal tussen 0 en 1: {rd.random()}')

# neemt 3 willekeurige waarden. Deze kunnen niet dezelfde zijn
l = [1,2,3,4]
print(f'sample: {rd.sample(l,3)}')

# neemt 3 willekeurige waarden. Deze kunnen dezelfde zijn
l = [1,2,3,4]
print(f'choices: {rd.choices(l, k=3)}')

# geeft een random element weer uit een string/list/tuple/set
num = rd.choice(range(10,100))
print(f'choice: {num}')