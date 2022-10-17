k = int(input('chawere xutnishna ricxvi: '))

while k < 10000 or k > 99999:
    print('ricxvi ar aris xutnishna \nscadet xelaxla')
    k = int(input('chawere xutnishna ricxvi: '))


a = k % 10
b = int(((k - a) / 10) % 10)
c = int(((k - b * 10**1 + a * 10**0) / 100) % 10)
d = int(((k - c * 10**2 + b * 10**1 + a * 10**0) / 1000) % 10)
e = int(((k - d * 10**3 + c * 10**2 + b * 10**1 + a * 10**0) / 10000) % 10)

pasuxi = (a + b + c + d + e) * 2

print(pasuxi)

































