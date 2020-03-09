
def create_list():
    a = []
    while True:
        try:
            t = int(input("Enter the number of arrays: "))
        except ValueError:
            print("Not a number. Try again.")
            continue
        try:
            d = int(input("Enter the number of elements in the array: "))
        except ValueError:
            print("Not a number. Try again.")
            continue

        for r in range(0, t):
            a.append([])
            for c in range(0, d):
                x = input("Enter the number of the " + str(r + 1) + " array: ")
                try:
                    num = float(x)
                except ValueError:
                    print("Not a number. Try again.")
                    continue

                a[r].append(num)
        break
    return a


def transform(a):
    k = []
    while True:
        try:
            z = int(input("Enter the minimum value: "))
        except ValueError:
            print("Not a number. Try again.")
            continue
        try:
            q = int(input("Enter the divisor: "))
        except ValueError:
            print("Not a number. Try again.")
            continue

        for b in a:
            for i, n in enumerate(b):
                if n >= z and (n / q) % 2 == 0:
                    k.append(n)
        break
    return k


def main():
    a = create_list()
    k = transform(a)
    print(k)


if __name__ == "__main__":
    main()
