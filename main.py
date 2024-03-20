# Case_3
# Developers: Zhambaldorzhieva A., Ryaguzova D., Zaitseva D.
#
import ru_local as ru

print(f'{ru.BEGGIN}\n1.{ru.FLOWERS}\n2.{ru.DESSERTS}\n3.{ru.DECOR}')
category = int(input(ru.CATEGORY))


def desire(present):
    """
    The function returns girl's preferences.
    """
    return (present == f'{ru.BIG} {ru.BOUQUET_OF_FLOWERS}' or present == f'{ru.STRAWBERRY}' or present ==
            f'{ru.RNG_ENGAGEMENT}')


def flowers():
    """
    The function returns the buket you selected.
    """
    wrap = 350
    delivery = 700
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
    match size:
        case 's':
            print(f'{ru.COST}: {3000 + wrap + delivery}')
        case 'm':
            print(f'{ru.COST}: {7200 + wrap + delivery}')
        case 'l':
            print(f'{ru.COST}: {11000 + wrap}')
        case 'xl':
            print(f'{ru.COST}: {13400 + wrap}')
    if type_bouquet == 1:
        if size == 's' or size == 'm':
            return f'{ru.MINI} {ru.BUNCH_OF_FLOWERS}'
        elif size == 'l' or size == 'xl':
            return f'{ru.BIG} {ru.BUNCH_OF_FLOWERS}'
    else:
        if size == 's' or size == 'm':
            return f'{ru.MINI} {ru.BOUQUET_OF_FLOWERS}'
        elif size == 'l' or size == 'xl':
            return f'{ru.BIG} {ru.BOUQUET_OF_FLOWERS}'


def desserts():
    """
    The function returns the desserts you selected.
    """
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

    money = int(input(ru.MONEY))
    print(f'{ru.DESSERT_CATEGORY}: \n1.{ru.CAKES}\n2.{ru.CAPCAKES}\n3.{ru.CANDIES}')
    category_dessert = int(input(ru.CATEGORY))
    if category_dessert == 1:
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
        cake = int(input(ru.CATEGORY))
        if cake == 1:
            dessert = f'{ru.NAPOLEON}'
            print(f'{ru.MONEY_SPENT} {napoleon}')
        elif cake == 2:
            dessert = f'{ru.CHEESECAKE}'
            print(f'{ru.MONEY_SPENT} {cheesecake}')
        elif cake == 3:
            dessert = f'{ru.TIRAMISU}'
            print(f'{ru.MONEY_SPENT} {tiramisu}')
        elif cake == 4:
            dessert = f'{ru.PRAGUE}'
            print(f'{ru.MONEY_SPENT} {prague}')
        else:
            dessert = f'{ru.RED_VELVET}'
            print(f'{ru.MONEY_SPENT} {red_velvet}')

    elif category_dessert == 2:
        if money > 4_000:
            print(f'{ru.BUDGET}:\n1.{ru.CHOCOLATE_CAPCAKE}\n2.{ru.VANILA_CAPCAKE}'
                  f'\n3.{ru.COFFEE_CAPCAKE}')
        elif money > 3_000:
            print(f'{ru.BUDGET}:\n2.{ru.VANILA_CAPCAKE}'
                  f'\n3.{ru.COFFEE_CAPCAKE}')
        elif money > 1_500:
            print(f'{ru.BUDGET}:\n3.{ru.COFFEE_CAPCAKE}')
        capcake = int(input(ru.CATEGORY))
        if capcake == 1:
            dessert = f'{ru.CHOCOLATE_CAPCAKE}'
            print(f'{ru.MONEY_SPENT} {chocolate_capcake}')
        elif capcake == 2:
            dessert = f'{ru.VANILA_CAPCAKE}'
            print(f'{ru.MONEY_SPENT} {vanila_capcake}')
        else:
            dessert = f'{ru.COFFEE_CAPCAKE}'
            print(f'{ru.MONEY_SPENT} {coffee_capcake}')

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
        candies = int(input(ru.CATEGORY))
        if candies == 1:
            dessert = f'{ru.STRAWBERRY}'
            print(f'{ru.MONEY_SPENT} {strawberry}')
        elif candies == 2:
            dessert = f'{ru.COCONUT}'
            print(f'{ru.MONEY_SPENT} {coconut}')
        elif candies == 3:
            dessert = f'{ru.CARAMEL}'
            print(f'{ru.MONEY_SPENT} {caramel}')
        else:
            dessert = f'{ru.CHOCOLATE}'
            print(f'{ru.MONEY_SPENT} {chocolate}')
    return dessert


def jewelry():
    """
    The function returns the jewelry you selected.
    """
    money = int(input(f'{ru.MONEY}: '))
    choice_met = input(f'{ru.METAL}: {ru.SILVER}, {ru.GOLD}\n{ru.METAL_VAR}: ')
    choice = int(input(f'{ru.JEWELRY}\n1.{ru.RINGS}\n2.{ru.BRASLETS}\n3.{ru.NECKLACES}'
                       f'\n{ru.CATEGORY}: '))
    match choice:
        case 1:
            choice_1 = int(input(f'{ru.VARIANT}\n1.{ru.RNG_WENZEL}\n2.{ru.RNG_FINGER}'
                                 f'\n3.{ru.RNG_ENGAGEMENT}\n{ru.CATEGORY}: '))
            print(f'{ru.CHOOSE}: {choice_1}')
        case 2:
            choice_1 = int(input(f'{ru.VARIANT}\n1.{ru.BRASLET_CHN}\n2.{ru.BRASLET_THN}'
                                 f'\n3.{ru.BRASLET_WCKR}\n{ru.CATEGORY}: '))
            print(f'{ru.CHOOSE}: {choice_1}')
        case 3:
            choice_1 = int(input(f'{ru.VARIANT}\n1.{ru.NECKLACE_KOLLAR}\n2.{ru.NECKLACE_CHKER}'
                                 f'\n3.{ru.NECKLACE_PRINCES}\n{ru.CATEGORY}: '))
            print(f'{ru.CHOOSE}: {choice_1}')

    if choice_met == 'золото' and money >= 10000:
        choice_smpl = int(input(f'{ru.SAMPLE}: 585, 500\n{ru.SAMP_VAR}: '))
        print(f'{ru.CHOOSE}: {choice_met} {choice_smpl}')
    elif choice_met == 'золото' and money < 10000:
        choice_smpl = int(input(f'{ru.SAMPLE}: 500\n{ru.SAMP_VAR}: '))
        print(f'{ru.CHOOSE}: {choice_met} {choice_smpl}')

    if choice_met == 'серебро' and money >= 10000:
        choice_smpl = int(input(f'{ru.SAMPLE}: 975, 925\n{ru.SAMP_VAR}: '))
        print(f'{ru.CHOOSE}: {choice_met} {choice_smpl}')
    elif choice_met == 'серебро' and money < 10000:
        choice_smpl = int(input(f'{ru.SAMPLE}: 925\n{ru.SAMP_VAR}: '))
        print(f'{ru.CHOOSE}: {choice_met} {choice_smpl}')
    print(f'{ru.CHOISE}')

    return choice_1


match category:
    case 1:
        final = flowers()
    case 2:
        final = desserts()
    case 3:
        final = jewelry()
print(f'{ru.CHOOSE}: {final}')
result = ru.RIGHT if desire(final) is True else ru.WRONG
print(result)
