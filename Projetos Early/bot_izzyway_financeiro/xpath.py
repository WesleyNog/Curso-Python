
modulos_xpaths = {
    # Botão para abrir lista dos Módulos
    'modulo': '/html/body/div[2]/div[1]/div[1]/nav/div/ul/li[3]/a/i',
    # Módulo de ESTOQUE
    'estoque': '/html/body/div[2]/div[1]/div[1]/nav/div/ul/li[3]/ul/li[4]/div/a/i',
    # Módulo FINANCEIRO
    'financeiro': '/html/body/div[2]/div[1]/div[1]/nav/div/ul/li[3]/ul/li[5]/div/a/i',
    # Módulo de MOVIMENTAÇÃO
    'movimentacao': '/html/body/div[2]/div[1]/div[1]/nav/div/ul/li[3]/ul/li[8]/div/a/i',
    # Módulo FISCAL
    'fiscal': '/html/body/div[2]/div[1]/div[1]/nav/div/ul/li[3]/ul/li[6]/div/a/i',
}

lojas_xpaths = {
    # Botão para abrir lista de Unidades/Lojas
    'loja': '/html/body/div[2]/div[1]/div[1]/nav/div/ul/li[2]/a/i',
    # Escolher Unidade/Loja - FABRICA
    'fabrica': '/html/body/div[2]/div[1]/div[1]/nav/div/ul/li[2]/ul/li[3]/div/div/div/div[2]/strong',
    # Escolher Unidade/Loja - EMBARQUE
    'embarque': '/html/body/div[2]/div[1]/div[1]/nav/div/ul/li[2]/ul/li[1]/div/div/div/div[2]/strong',
    # Escolher Unidade/Loja - IGUATEMI
    'iguatemi': '/html/body/div[2]/div[1]/div[1]/nav/div/ul/li[2]/ul/li[4]/div/div/div/div[2]/strong',
    # Escolher Unidade/Loja - RIOMAR
    'riomar': '/html/body/div[2]/div[1]/div[1]/nav/div/ul/li[2]/ul/li[7]/div/div/div/div[2]/strong',
    # Escolher Unidade/Loja - QUARTIER
    'quartier': '/html/body/div[2]/div[1]/div[1]/nav/div/ul/li[2]/ul/li[6]/div/div/div/div[2]/strong',
    # Escolher Unidade/Loja - VICENTE LEITE
    'vicente': '/html/body/div[2]/div[1]/div[1]/nav/div/ul/li[2]/ul/li[8]/div/div/div/div[2]/strong',
    # Escolher Unidade/Loja - MAISON
    'maison': '/html/body/div[2]/div[1]/div[1]/nav/div/ul/li[2]/ul/li[5]/div/div/div/div[2]/strong',
    # Escolher Unidade/Loja - EVENTOS
    'evento': '/html/body/div[2]/div[1]/div[1]/nav/div/ul/li[2]/ul/li[2]/div/div/div/div[2]/strong',
}


cp_xpaths = {
    # Acessar o CONTAS A PAGAR
    'contas_pagar': '/html/body/div[2]/nav/div[1]/ul/li[65]/a/i',
    # Acessar o CONTAS A RECEBER
    'contas_receber': '/html/body/div[2]/nav/div[1]/ul/li[64]/a/i',
    # Novo lancamento de CONTAS A PAGAR
    'novo_cp': '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/button',
    # Inserção de LANCAMENTO SIMPLES
    'lancamento_simples': '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/ul/li[1]/a/strong',
    # Inserção de LANCAMENTO COMPLETO
    'lancamento_completo': '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/ul/li[2]/a/strong',
    # Inserir um PLANO DE CONTAS
    'plano_contas': '/html/body/div[1]/div/div/div[2]/form/div[1]/div/div/div[1]/div/input',
    # Inserir um CENTRO DE RESULTADOS
    'centro_resultados': '/html/body/div[1]/div/div/div[2]/form/div[2]/div/div/div[1]/div/input',
    # Inserir o NÚMERO DO DOCUMENTO
    'documento': '/html/body/div[1]/div/div/div[2]/form/div[4]/div/div/div/input',
    # Informar PARTICIPANTE
    'participante': '/html/body/div[1]/div/div/div[2]/form/div[5]/div/div/div[1]/div/input',
    # Informar DATA DE EMISSÃO
    'emissao': '//*[@id="Emissao"]',
    # Informar DATA DE VENCIMENTO
    'vencimento': '//*[@id="Vencimento"]',
    # Informar o VALOR da operação
    'valor': '//*[@id="ModalValor"]',
    # Conceder DESCONTO
    'desconto': '/html/body/div[1]/div/div/div[2]/form/div[8]/div/div/div[2]/input',
    # Conceder ACRÉSCIMO
    'acrescimo': '/html/body/div[1]/div/div/div[2]/form/div[9]/div/div/div[1]/input',
    # Campo para informar um HISTÓRICO
    'historico': '//*[@id="Historico"]',
    # Inserir uma FORMA DE PAGAMENTO
    'forma_pagamento': '/html/body/div[1]/div/div/div[2]/form/div[14]/div/div/div[1]/select',
    # Informar a DATA DO PAGAMENTO
    'data_pagamento': '//*[@id="PrevisaoData"]',
    # SALVAR o lançamento SEM FINALIZA-LO
    'salvar': '/html/body/div[1]/div/div/div[3]/button[2]',
    # SALVAR E FINALIZAR o lancamento
    'salvar_finalizar': '/html/body/div[1]/div/div/div[3]/button[3]',
}