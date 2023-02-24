def power(N, P):
    if P == 0:
        return 1
    return (N*power(N, P-1))

if __name__ == '__main__':
    N = int(input("Enter the base number: "))
    P = int(input("Enter the power: "))

    print(power(N, P))