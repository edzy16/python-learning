print("enter the first no:")
first = int(input())
print("enter the 2nd number:")
second = int(input())
print("select operation \ 1. addition \ 2. subtraction \ 3. mutiplication \ 4 division \ 5 modulus")
n = int(input())
if n == 1 :
    print(first + second) 
elif n == 2 :
    print(first - second)
elif n == 3 :
    print(first * second)
elif n == 4 :
    print(first / second)
else :
    print(first % second)