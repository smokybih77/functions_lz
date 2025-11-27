def chet(n):
    if n % 2 == 0:
        print('Четное!')
    else:
        print('Нечетное!')

def main():
    n = int(input('Введите число для проверки на четность: '))
    chet(n)
if __name__ == "__main__":
    main()