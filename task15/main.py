def get_numbers(n, prompt="Enter number: "):
    a = []
    while n > 0:
        x = input(prompt)
        try:
            num = float(x)
        except ValueError:
            print("Not a number. Try again.")
            continue
        a.append(num)
        n -= 1

    return a


def transform(a):
    k1 = []
    k2 = []
    k3 = []
    k4 = []
    for i, x in enumerate(a):
        if i % 2 == 0: # Even
            if x < 0:
                k2.append(x)
            else:
                k4.append(x)
        else:          # Odd
            if x >= 0:
                k1.insert(0, x)
            else:
                k3.insert(0, x)

    k1.extend(k2)
    k1.extend(k3)
    k1.extend(k4)

    return k1


def main():
    g = get_numbers(1, "Enter number of elements: ")
    a = get_numbers(g[0])
    k = transform(a)
    print(k)


if __name__ == "__main__":
    main()
