def sq(n):
    for i in range(n):
        yield(i*i)
c = sq(10)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

