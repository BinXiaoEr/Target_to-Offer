a=5
b=7
#print(5^7)


def add(n, m):
    while m:
        summ = n ^ m#异或不考虑进位 不同为0
        print(summ)
        carry = (n & m) << 1#产生进位 左移相当于加10
        print(carry)
        m = carry
        n = summ

    return n
#print(add(7,3))

a='\u006d\u0070\u0034'
print(a)
print(type(a.encode('utf8')))
print(type(a.encode('utf8').decode('utf8')))