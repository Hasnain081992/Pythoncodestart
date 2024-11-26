for n in range(2,12):
    for x in range(2,n):
        if n % x ==0:
            print(f"{n} is equal to {x} * {n//x}")
            break

#  