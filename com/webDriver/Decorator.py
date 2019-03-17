

def div(a, b):
    print(a/b)



def super_div(func):

    def inner(a, b):
        if a < b:
            a, b = b, a
            return func(a, b)
    return inner



div = super_div(div)

div(4, 6)
