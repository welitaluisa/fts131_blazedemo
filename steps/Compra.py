from behave import *

@given('que acesso o site Blazedemo')
def que_acesso_o_site_Blazedemo(context):
    print('Passo 1 - Abriu o site')


@when('pesquiso passagens de {origem} a {destino}')
def pesquiso_passagens_de_origem_a_destino(context, origem, destino):
    print(f' Passo 2 - Pesquisou passagem de {origem} para {destino}')


@when('seleciono o primeiro voo')
def seleciono_o_primeiro_voo(context):
    print('Passo 3 - Seleciono o primeiro voo ')

@when('preencho os dados de pagamento')
def preencho_os_dados_de_pagamento(context):
    print(' Passo 4 - Preencheu os dados do pagamento')

@then('valido se a passagem foi emitida')
def valido_se_a_passagem_foi_emitida(context):
    print('Passo 5 - Validou se a passagem foi emitida')
