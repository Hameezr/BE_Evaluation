def primeNumber(limit):
    for i in range(1, limit+1):
        flag = True
        for j in range(2, i):
            if ((i % j == 0) and i != j):
                flag = False
                break
        if (flag):
            print(i, end=' ')


def main():
    num = int(input("Enter a number: "))
    primeNumber(num)


if __name__ == "__main__":
    main()
