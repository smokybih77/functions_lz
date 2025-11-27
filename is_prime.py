
#Простота
def prost(p):
    k = 0
    for i in range(2, p // 2+1):
        if (p % i == 0):
            k = k+1
    if (k <= 0):
            print('Число является простым')
    else:
            print('Число не является простым')


def main():
    p=int(input('Введите число:  '))
    prost(p)
if __name__ == "__main__":
    main()

