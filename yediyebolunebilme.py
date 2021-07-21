numbers = [18,21,14,84,65,35,10,20,28,42,24,91,5,7,54,69]
len_ = len(numbers)
sorted_ = []
i = 0
while i <= len_ - 1:
    a = min(numbers)
    sorted_.append(a)
    numbers.remove(a)
    i += 1
counter = 0    
for x in sorted_:
    if x % 7 == 0:
        print(x," is a number divisible by five")
        counter += 1
print("Number divisible by five is:",counter)