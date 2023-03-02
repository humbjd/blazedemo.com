from behave import given, when, then

@given(u'que acesso o site Blazedemo')
def step_impl(context):

    print('Passo 1 - Acessou o site Blazedemo')


@when(u'seleciono a a cidade de origem como "São Paolo"')
def step_impl(context):

    print('Passo 2 - Selecionou a cidade de origem')


@when(u'seleciono a cidade de destino como "Rome"')
def step_impl(context):

    print('Passo 3 - Selecionou a cidade de destino')


@when(u'clico no botao Find Flights')
def step_impl(context):

    print('Passo 4 - Clicou no botão Find Flights')


@then(u'sou direcionado para a pagina de selecao de voos')
def step_impl(context):

    print('Passo 5 - Direcionou para a pagina de pagamento')

@when(u'seleciono o primeiro voo')
def step_impl(context):

    print('Passo 6 - Selecionou o primeiro voo')

@then(u'sou direcionado para a pagina de pagamento')
def step_impl(context):

    print('Passo 7 - Direcionou para a pagina de pagamento')

@when(u'preencho os dados para o pagamento')
def step_impl(context):

    print('Passo 8 - Preencheu os dados para o pagamento ')

@when(u'clico no botao Puchase Flight')
def step_impl(context):

    print('Passo 9 - Clicou no botão Purchase Flight')

@then(u'sou direcionado para a pagina de confirmacao')
def step_impl(context):

    print('Passo 10 - Direcionou para a pagina de confirmação')

@when(u'seleciono a a cidade de origem como "São Paolo" para "Rome"')
def step_impl(context):

    print('Passo 2c - Seleciocou a cidade de origem e destino')