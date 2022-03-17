# dictionary 자료형 연습

# dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
# print(dic)

# a = {'a': [1, 2, 3]}
# a = {1: 'a'}
#
# a[2] ='b'
#
# print(a)

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}

print(a.keys())
print(a.values())
print(a.items())
# print(a.clear())
print(a.get('name'))
print(a.get('phone'))
print('name' in a)
print('email' in a)