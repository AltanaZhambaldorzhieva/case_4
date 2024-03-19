# Case_3
# Developers: Zhambaldorzhieva A., Ryaguzova D., Zaitseva D.
#
import ru_local as ru


def desire(present):
    return present == ru.ENGAGEMENT_RING


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




#result = ru.RIGHT if desire(choice) is True else ru.WRONG
#print(result)
