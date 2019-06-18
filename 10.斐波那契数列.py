def Fibonacci_Digui(n):
    if n ==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci_Digui(n-1)+Fibonacci_Digui(n-2)
def Fiblnacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    first = 0
    seconde = 1
    result = None
    for i in range(2,n+1):
        result=first+seconde
        first=seconde
        seconde=result
    return result

def tiaotaijie(n):
    if n<3:
        return n
    first=1
    second=2
    result=None
    for i in range(3,n+1):
        result=first+second
        first=second
        second=result
    return result
print(Fibonacci_Digui(5))
print(Fiblnacci(5))
print(tiaotaijie(4))