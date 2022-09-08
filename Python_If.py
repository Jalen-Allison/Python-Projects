

num1 = 10
key = False

if num1 == 12:
    if key: 
        print('Num1 is equal to Tweleve and they have the key!')
    else:
        print('Num1 is equal to Tweleve and they DO NOT have the key!')
elif num1 < 12:
    print('Num1 is less than Tweleve!')
else:
    print('Num1 is NOT equal to Tweleve!')

    
a = 32
b = 32
if b > a:
    print("b is greater than a")
elif b < a:
    print("b is smaller than a")
else:
    print(" a and b are equal")

x = isinstance("Hello", (float, int, list, dict, tuple))
print(x)
