def gradus(c):
    far = c * (9/5) + 32
    print('Температура в фаренгейтах: ', far)


def main():
    c = float(input('Введите температуру в цельсиях: '))
    gradus(c)
if __name__ == "__main__":
    main()