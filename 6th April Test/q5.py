def sum_series(n, a):
    if n == 1:
        return 1
    else:
        return n * n / a * n + sum_series(n - 1, a)

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
sum1 = sum_series(num1, num2)

print(sum1)


def sum_series2(n):
    if n == 1:
        return 1
    else:
        return (-1) ** (n - 1) * n + sum_series2(n - 1)

num = int(input("Enter a number: "))
sum2 = sum_series2(num)
print(sum2)