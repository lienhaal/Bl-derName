summe = 0
x = 1
while x <= 4000000:
    summe += x
    x += x
print("Die Summe der Fibonacci-Zahlen bis 4 Millionen beträgt " + str(summe))