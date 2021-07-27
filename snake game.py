x = int(input("Enter row and column size:"))
i = 1
a = 0 # yılanın boyu ilk döngüde zaten 1 olduğu için a değeri -1 olarak tanımlandı.
while 2 ** i <= x ** 2: # 2 ** 1 formulü yılanın boyunu verir.
    a += 1
    i += 1
print("snakefill:", x ** 2, "and snake can eat", a , "times before it runs out of space in the game screen.")