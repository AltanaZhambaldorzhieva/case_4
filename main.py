# Case_3
# Developers: Zhambaldorzhieva A., Ryaguzova D., Zaitseva D.
#
import ru_local as ru


def desire(present):
    return present == ru.RNG_ENGAGEMENT


def flowers():
    wrap = 350
    delivery = 1000
    money = int(input(ru.MONEY))
    if money > 13_000:
        print(f'{ru.POSSIBLE_SIZES} S, M, L, XL')
    elif money > 9_000:
        print(f'{ru.POSSIBLE_SIZES} S, M, L')
    elif money > 5_000:
        print(f'{ru.POSSIBLE_SIZES} S, M')
    else:
        print(f'{ru.POSSIBLE_SIZES} S')
    type_bouquet = input(f'{ru.TYPE_BOUQUET}\n1.{ru.BUNCH_OF_FLOWERS}\n2.{ru.BOUQUET_OF_FLOWERS}')
    size = input(ru.SIZE).lower()



def desserts():
    biscuit_cake = 2000
    curd_cake = 1800
    waffel_cake = 1500
    chocolate_filling = 500
    berry_filling = 800
    cream_filling = 650
    decoration_flowers = 750
    decoration_berry = 800
    decoration_chocolate = 600
    money = int(input(ru.MONEY))
    print(f'{ru.DESSERT_CATEGORY}: \n1.{ru.CAKES}\n2.{ru.CAPCAKES}\n3.{ru.CANDIES}')

def jewelry():
    choice = int(input(f'{ru.JEWELRY}:\n1.{ru.RINGS}\n2.{ru.BRASLETS}\n3.{ru.NECKLACES}\n{ru.CATEGORY_JEWELRY}:'))
    match choice:
        case 1:
            print(f'{ru.CATEGORY_RINGS}:\n1.{ru.RNG_WENZEL}\n2.{ru.RNG_FINGER}\n3.{ru.RNG_ENGAGEMENT}')
        case 2:
            print(f'{ru.CATEGORY_BRASLETS}:\n1.{ru.BRASLET_CHN}\n2.{ru.BRASLET_THN}\n3.{ru.BRASLET_WCKR}')
        case 3:
            print(f'{ru.CATEGORY_NECKLACE}:\n1.{ru.NECKLACE_KOLLAR}\n2.{ru.NECKLACE_CHKER}\n3.{ru.NECKLACE_PRINCES}')

#result = ru.RIGHT if desire(final) is True else ru.WRONG
#print(result)

