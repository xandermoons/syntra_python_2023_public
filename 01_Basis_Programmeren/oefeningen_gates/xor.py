# 'X' staat voor exclusive --> exclusive or = enkel verschillend

def XOR_gate(a,b):
    return a != b

print(XOR_gate(0,0)) # 0
print(XOR_gate(0,1)) # 1
print(XOR_gate(1,0)) # 1
print(XOR_gate(1,1)) # 0