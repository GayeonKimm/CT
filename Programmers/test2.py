temp = []
for i in range(15):
    temp.append('0'*(17-len(bin(i)[2:]))+bin(i)[2:])
print(temp)
print(bin(100000))