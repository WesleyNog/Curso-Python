def gerador(n=0, maximun=10):
    while True:
        yield n
        n += 1

        if n >= maximun:
            return


gen = gerador(maximun=50)
for n in gen:
    print(n)