


def fab(n):
    a = 0
    b = 1

    if n <= 0:
        print("provide valid  number")

    if n == 1:
        print(a)



    if n > 1:

        print(a)
        print(b)

        for value in range(2, n):

            c = a + b
            a = b
            b = c
            print(c)

fab(10)

