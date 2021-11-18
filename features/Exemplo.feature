Feature: Compra de Passagem Aerea
  Scenario: Viagem de Sao Paulo a New York
    Given que acesso o site Blazedemo

    # Parametros fixos

    When pesquiso passagens de 'Sao Paulo' a 'New York'

    # Lista de paramentros

   When pesquiso passagens de <origem> a < destino

        | origem      | destino
        | 'Sao Paulo' | 'New York'

     And  Seleciono o primeiro voo
     And  preencho os dados de pagamento como <cartao> < titulo> <CVV>

        | cartao      | titulo    | CVY
        | '9999999'   | 'New York'| 'visa'