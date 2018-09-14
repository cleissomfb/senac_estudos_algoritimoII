from behave import given, when, then
import calcula_numero_meio


@given('uma lista com os numeros (3,1,2)')
def dada_num_esquerda(context):
    context.lista_num1 = [3, 1, 2]


@when('queremos saber o numero da esquerda')
def saber_num_esquerda(context):
    lista1 = context.lista_num1
    context.num_esquerda = calcula_numero_meio.num_esquerda(lista1)


@then('o resultado e 3')
def resultado_num_esquerda(context):
    assert context.num_esquerda == 3

# ---------------------------------------------------------


@given('uma lista com os numeros (9,8,7)')
def dada_lista_direita(context):
    context.lista_num2 = [9, 8, 7]


@when('queremos saber o numero da direita')
def saber_num_direita(context):
    lista2 = context.lista_num2
    context.num_direita = calcula_numero_meio.num_direita(lista2)


@then('o resultado e 7')
def resultado_num_direita(context):
    assert context.num_direita == 7

# ------------------------------------------------------------


@given('uma lista com os numeros (6,5,4)')
def dada_lista_meio(context):
    context.lista_num3 = [6, 5, 4]


@when('queremos saber o numero que esta no meio')
def saber_num_meio(context):
    lista3 = context.lista_num3
    context.num_meio = calcula_numero_meio.num_meio(lista3)


@then('o resultado e 5')
def resultado_num_meio(context):
    assert context.num_meio == 5
