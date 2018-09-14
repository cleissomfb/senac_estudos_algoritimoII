# Digitar três números e separa o númnero da esquerda, do meio e o da esquerda.

# lista_num = [9, 8, 7]


def num_esquerda(lista_num):
    esquerda_num = lista_num[0]
    for indice_esquerda in lista_num:
        if indice_esquerda < esquerda_num:
            esquerda_num = indice_esquerda
    return esquerda_num


def num_direita(lista_num):
    direita_num = lista_num[0]
    for indice_direita in lista_num:
        if indice_direita > direita_num:
            direita_num = indice_direita
    return direita_num


def num_meio(lista_num):
    esquerda_num = num_esquerda(lista_num)
    direita_num = num_direita(lista_num)
    i = 0
    meio_num = lista_num[0]
    while meio_num == direita_num or meio_num == esquerda_num:
        i += 1
        meio_num = lista_num[i]
    return meio_num


# print("Lista de números: ",str(lista_num).strip("[]"))
# print("Número da direita: ", num_direita(lista_num))
# print("Número da esquerda: ", num_esqueda(lista_num))
# print("Número do meio: ", num_meio(lista_num))
