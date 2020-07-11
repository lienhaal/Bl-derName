summe = 0
for i in range (0,1000):
    if i % 3 == 0 or i % 5 == 0:
        summe += i
print(summe)