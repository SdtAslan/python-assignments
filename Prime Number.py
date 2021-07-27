y = input("Enter a number > learn to is it prime number")
if y.isdigit():
    x = int(y)
    a = False
    if x < 2:
        a = True
    elif x == 2:
        a = False
    elif x > 2:
        for i in range(2, x):
            if (x % i) == 0:
                a = True
                
    if a:
        print(x, "is not a prime number")
    else:
        print(x, "is a prime number")
else:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")