# Case_3
# Developers: Zhambaldorzhieva A., Ryaguzova D., Zaitseva D.
#
import ru_local as ru


def desire(present):
    return present == ru.RNG_ENGAGEMENT


def flowers():
    money = int(input(ru.BUDGET))
    if money > 13_000:
        print(f'{ru.POSSIBLE_SIZES} S, M, L, XL')
    elif money > 9_000:
        print(f'{ru.POSSIBLE_SIZES} S, M, L')
    elif money > 5_000:
        print(f'{ru.POSSIBLE_SIZES} S, M')
    else:
        print(f'{ru.POSSIBLE_SIZES} S')
    size = input(ru.SIZE).lower()
    flowers =
    match size:
        case 's':
            print(1)
        case 'm':
            print()
        case 'l':
            print()
        case 'xl':
            print()



import ru_local as ru
choise = int(input(f'{ru.CATEGORY_JEWELRY}:\n1.{ru.RINGS}\n2.{ru.BRASLETS}\n3.{ru.NECKLACES}'))
def jewelry():
    match choise:
        case 1:
            print(f'{ru.CATEGORY_RINGS}:\n1.{ru.RNG_WENZEL}\n2.{ru.RNG_FINGER}\n3.{ru.RNG_ENGAGEMENT}')
        case 2:
            print(f'{ru.CATEGORY_BRASLETS}:\n1.{ru.BRASLET_CHN}\n2.{ru.BRASLET_THN}\n3.{ru.BRASLET_WCKR}')
        case 3:
            print(f'{ru.CATEGORY_NECKLACE}:\n1.{ru.NECKLACE_KOLLAR}\n2.{ru.NECKLACE_CHKER}\n3.{ru.NECKLACE_PRINCES}')

#result = ru.RIGHT if desire(choice) is True else ru.WRONG
#print(result)
