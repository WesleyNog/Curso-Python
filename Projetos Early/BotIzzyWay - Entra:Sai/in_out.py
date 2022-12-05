import func as f

URL = 'https://app.izzyway.com.br/Account/Login#'
LOGIN, PASSOWORD = 'adm4@briejer.com.br', '225368'


f.driver.get(URL)
f.logar(LOGIN, PASSOWORD)
f.loja()
f.modulo_estoque() 
f.acerto_ajuste()
f.new_operacion('saida')
f.data_operation('22112022', 'riomar', 'desperdicio')