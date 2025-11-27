def circle(r):
    s = 3.14 * r ** 2
    c = 2 * 3.14 * r
    print('Площадь:', s, 'Длина окружности', c)

def main():
    r = float(input('Введите радиус окружности: '))
    circle(r)
if __name__ == "__main__":
    main()
