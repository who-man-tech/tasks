# Задание №14


def fill():
    a = []
    for r in range(0, 6):
        a.append([])
        for c in range(0, 6):
            if (r + 1) % 3 == 0:
                a[r].append(0)
            else:
                a[r].append(1)

    return a


def main():
    a = fill()
    print(a)


if __name__ == "__main__":
    main()
