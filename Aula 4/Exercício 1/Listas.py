import random


def lista_random():
    L = [random.randint(0, 100) for x in range(random.randint(10, 100))]
    return L


def conversao_true_false():
    for x in lista_random():
        if x % 2 == 0:
            print(str(x).strip('[]'), " - True")
        else:
            print(str(x).strip('[]'), " - False")


conversao_true_false()
