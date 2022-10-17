"""
a = 0
b = 0
c = 0
d = 0
e = 0

#x = [a, b, c, d, e]

[a, b, c, d, e] = int(input("chawere xutnishna ricxvi: "))

x = [a, b, c, d, e]
if x < 10000 or x > 99999:
    print('ricxvi ar aris xutnishna')
    int(input('scadet xelexla: '))
    if x < 10000 or x > 99999:
        print("tqven gadzevebuli xart sistemidan orjer arasworad chaweristvis")

else:
#    [a, b, c, d, e] = x

   # x = [a, b, c, d, e]
    print(x)
    print(a)

==========================================================================

k = input("chawere ricxvi: ")

[" "," "] = k


print(k)


a = 1
b = 2
c = 3
d = 4
e = 5

num = [a,b,c,d,e]
x = 12345
#num = x

print(x)
print(num)












a = 0
b = 0
c = 0
d = 0
e = 0

k = 34562

a * 10 ** 4 + b * 10 ** 3 + c * 10 ** 2 + d * 10 ** 1 + e * 10 ** 0 == k

a = k [1]


x = a * 10 ** 4 + b * 10 ** 3 + c * 10 ** 2 + d * 10 ** 1 + e * 10 ** 0



print(x)
print(k)
print(a)
"""















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

































