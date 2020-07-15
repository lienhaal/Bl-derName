primes = []
teileranzahl = 0
for i in range (3,600):
    for pruefzahl in range (1,i):
        if i % pruefzahl == 0:
            teileranzahl += 1
    if teileranzahl == 2:
        primes.append(i)
    teileranzahl = 0
print(primes)