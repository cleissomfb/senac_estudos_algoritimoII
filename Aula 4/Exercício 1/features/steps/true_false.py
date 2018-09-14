from behave import given, when, then
import Listas


@given('uma lista de números randomicos')
def dada_lista(context):
    context.lista = [0, 1, 2, 3]


@when('verifico se são pares ou impares')
def verifica_true_false(context):
    context.verifica = Listas.conversao_true_false()


@then('todos os pares são True e todos os impares são False')
def conversao_true_false(context):
    assert context.verifica == [True, False, True, False]
