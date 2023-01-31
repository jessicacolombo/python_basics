def div_by_zero():
    a = 1
    b = 0

    return a / b


def unexisting_key():
    my_dict = {"name": "Alex", "module": "M5"}

    return my_dict["address"]


def unexisting_index():
    my_list = [0, 1]

    return my_list[5]


def misterious_error():
    a = 5

    return a.capitalize()


if __name__ == "__main__":
    try:
        div_by_zero()
    except ZeroDivisionError:
        print('não é possivel dividir por 0')

    try:
        unexisting_key()
    except KeyError:
        print('buscou uma chave que nao existe')

    try:
        unexisting_index()
    except IndexError:
        print('buscou um index que nao existe')

    try:
        misterious_error()
    except AttributeError:
        print('a propriedade .capitalize() é exclusiva de objetos da classe string')
