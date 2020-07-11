summe = 0
n = 1
while n <= 4000000:
    n = n += n
    if n % 2 == 0:
        summe += n
print(summe)