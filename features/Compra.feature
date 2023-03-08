@compra_passagem
Feature: Compra de Passagem Aerea
  # Descreve a compra pelo site Blazedemo.com
  # E2E = End to End = Ponta a ponta
  Scenario: De São Paulo a Roma
    Given que acesso o site Blazedemo
    When seleciono a a cidade de origem como "São Paolo"
    And seleciono a cidade de destino como "Rome"
    And clico no botao Find Flights
    Then sou direcionado para a pagina de selecao de voos
    When seleciono o primeiro voo
    Then sou direcionado para a pagina de pagamento
    When preencho os dados para o pagamento
    And clico no botao Puchase Flight
    Then sou direcionado para a pagina de confirmacao




  Scenario Outline: De São Paulo a Roma compacto
    Given que acesso o site Blazedemo
    When seleciono a a cidade de origem como "São Paolo" para "Rome"
    Then sou direcionado para a pagina de selecao de voos
    When seleciono o primeiro voo
    Then sou direcionado para a pagina de pagamento
    When preencho os dados para o pagamento
    And clico no botao Puchase Flight
    Then sou direcionado para a pagina de confirmacao

    Examples:
      |origem       | destino       |
      |Philadephia  | Buenos Aires  |
      |Mexico City  | Cairo         |

