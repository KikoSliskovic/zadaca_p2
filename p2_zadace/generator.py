def even_odd_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i, "paran"
        else:
            yield i, "neparan"

n = 10
numbers = even_odd_numbers(n)

for number, parity in numbers:
    print(number, "je", parity)
