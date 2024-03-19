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
    size = input(ru.SIZE).lower()
    type_bouquet = input(f'{ru.TYPE_BOUQUET}\n1.{ru.BUNCH_OF_FLOWERS}\n2.{ru.BOUQUET_OF_FLOWERS}\n')


def desserts():
    napoleon = 4500
    cheesecake = 3600
    tiramisu = 2850
    prague = 1980
    red_velvet = 999

    chocolate_capcake = 3999
    vanila_capcake = 2899
    coffee_capcake = 1200

    strawberry = 5200
    coconut = 4150
    caramel = 3499
    chocolate = 1200

    sum = 0
    money = int(input(ru.MONEY))
    print(f'{ru.DESSERT_CATEGORY}: \n1.{ru.CAKES}\n2.{ru.CAPCAKES}\n3.{ru.CANDIES}')
    category = int(input(ru.CATEGORY))
    if category == 1:
        if money > 5_000:
            print(f'{ru.BUDGET}:\n1.{ru.NAPOLEON}\n2.{ru.CHEESECAKE}\n3.{ru.TIRAMISU}'
                  f'\n4.{ru.PRAGUE}\n5.{ru.RED_VELVET}')
        elif money > 4_000:
            print(f'{ru.BUDGET}:\n2.{ru.CHEESECAKE}\n3.{ru.TIRAMISU}'
                  f'\n4.{ru.PRAGUE}\n5.{ru.RED_VELVET}')
        elif money > 3_000:
            print(f'{ru.BUDGET}:\n3.{ru.TIRAMISU}'
                  f'\n4.{ru.PRAGUE}\n5.{ru.RED_VELVET}')
        elif money > 2_000:
            print(f'{ru.BUDGET}:\n4.{ru.PRAGUE}\n5.{ru.RED_VELVET}')
        else:
            print(f'{ru.BUDGET}:\n5.{ru.RED_VELVET}')
        cake = int(input(ru.DESSERT_CATEGORY))
        if cake == 1:
            sum = napoleon
        elif cake == 2:
            sum = cheesecake
        elif cake == 3:
            sum = tiramisu
        elif cake == 4:
            sum = prague
        else:
            sum = red_velvet

    elif category == 2:
        if money > 4_000:
            print(f'{ru.BUDGET}:\n1.{ru.CHOCOLATE_CAPCAKE}\n2.{ru.VANILA_CAPCAKE}'
                  f'\n3.{ru.COFFEE_CAPCAKE}')
        elif money > 3_000:
            print(f'{ru.BUDGET}:\n2.{ru.VANILA_CAPCAKE}'
                  f'\n3.{ru.COFFEE_CAPCAKE}')
        elif money > 1_500:
            print(f'{ru.BUDGET}:\n3.{ru.COFFEE_CAPCAKE}')
        capcake = int(input(ru.DESSERT_CATEGORY))
        if capcake == 1:
            sum = chocolate_capcake
        elif capcake == 2:
            sum = vanila_capcake
        else:
            sum = coffee_capcake

    else:
        if money > 5_000:
            print(f'{ru.BUDGET}:\n1.{ru.STRAWBERRY}\n2.{ru.COCONUT}\n3.{ru.CARAMEL}'
                  f'\n4.{ru.CHOCOLATE}')
        elif money > 4_000:
            print(f'{ru.BUDGET}:\n2.{ru.COCONUT}\n3.{ru.CARAMEL}'
                  f'\n4.{ru.CHOCOLATE}')
        elif money > 3_000:
            print(f'{ru.BUDGET}:\n3.{ru.CARAMEL}'
                  f'\n4.{ru.CHOCOLATE}')
        else:
            print(f'{ru.BUDGET}:\n4.{ru.CHOCOLATE}')
        candies = int(input(ru.DESSERT_CATEGORY))
        if candies == 1:
            sum = strawberry
        elif candies == 2:
            sum = coconut
        elif candies == 3:
            sum = caramel
        else:
            sum = chocolate


def jewelry():
    choice = int(input(f'{ru.JEWELRY}\n1.{ru.RINGS}\n2.{ru.BRASLETS}\n3.{ru.NECKLACES}\n{ru.CATEGORY}: '))
    match choice:
        case 1:
            choice_1 = int(input(f'{ru.VARIANT}\n1.{ru.RNG_WENZEL}\n2.{ru.RNG_FINGER}\n3.{ru.RNG_ENGAGEMENT}'
                                 f'\n{ru.CATEGORY}: '))
        case 2:
            choice_1 = int(input(f'{ru.VARIANT}\n1.{ru.BRASLET_CHN}\n2.{ru.BRASLET_THN}\n3.{ru.BRASLET_WCKR}'
                                 f'\n{ru.CATEGORY}: '))
        case 3:
            choice_1 = int(input(f'{ru.VARIANT}\n1.{ru.NECKLACE_KOLLAR}\n2.{ru.NECKLACE_CHKER}\n3.{ru.NECKLACE_PRINCES}'
                                 f'\n{ru.CATEGORY}: '))


# result = ru.RIGHT if desire(final) is True else ru.WRONG
# print(result)

flowers()
