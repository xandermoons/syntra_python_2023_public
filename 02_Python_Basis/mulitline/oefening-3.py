# Write a function that, given a string prints the string as a comment. Use triple auotes for the mulit-line string

def multiline(string):
    print(f'''---
{string}
---
          ''')

multiline('testtest')
