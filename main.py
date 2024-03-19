# Case_3
# Developers: Zhambaldorzhieva A., Ryaguzova D., Zaitseva D.
#
import ru_local as ru


def desire(present):
    return present == ru.ENGAGEMENT_RING


def flowers():
    money = int(input('На какую сумму вы бы хотели приобрести букет?'))
    if money > 13_000:
        print('Возможные размеры букетов, согласно вашему бюджету: S, M, L, XL')
    elif money > 9_000:
        print('Возможные размеры букетов, согласно вашему бюджету: S, M, L')
    elif money > 5_000:
        print('Возможные размеры букетов, согласно вашему бюджету: S, M')
    else:
        print('Возможные размеры букетов, согласно вашему бюджету: S')
    size = input('Выберете размер букета')
