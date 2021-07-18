x = (input("Enter a positive number to find out if it's an Armstrong number"))
if x.strip().isdigit():
    b = int(x)
    a = list(x)
    n = len(a)
    i = 0
    y = 0
    while i < n:
        z = (int(a[i]) ** n) 
        y += z
        i += 1
    if b == y:
        print("The number you entered:",x,"is an amstrong numbery")
    else:
        print("The number you entered:",x,"is not an amstrong numbery")
else:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")

#https://github.com/SdtAslan/python-assignments.git

