
def get_num(prompt, real=True):
    while True:
        try:
            if real:
                return float(input(prompt))
            return int(input(prompt))
        except ValueError:
            print("Not a number. Try again.")



def create_list():
    a = []

    t = get_num("Enter the number of rows: ", False)
    d = get_num("Enter the number of elements in the row: ", False)
    
    for r in range(0, t):
        a.append([])
        for c in range(0, d):
            a[r].append(get_num("Enter the value of the " + str(r + 1) + "," + str(c + 1) + " element: "))

    return a


def transform(a):
    k = []
    z = get_num("Enter the minimum value: ")
    q = get_num("Enter the divisor: ", False)

    for b in a:
        for i, n in enumerate(b):
            if n >= z and (i / q) % 2 == 0:
                k.append(n)

    return k


def main():
    a = create_list()
    k = transform(a)
    print(k)


if __name__ == "__main__":
    main()
