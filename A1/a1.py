numbers = range(1, 101)
for n in numbers:
    risp = ''
    if n % 3 == 0:
        risp = 'fizz '
    if n % 5 == 0:
        risp += 'buzz'
    if risp != '':
        print(risp)
    else:
        print(n)
