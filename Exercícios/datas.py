from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

emprestimo = 1000000
data_inicio = datetime(2020, 11, 20)
format_data_inicio = data_inicio.strftime('%d/%m/%Y')
delta = data_inicio + relativedelta(years=5)
data_dif = (delta - data_inicio).days
moth = data_dif / 30.433333333333334
valor_parcela = emprestimo / moth
format_valor_parcela = f'R$ {valor_parcela:,.2f}'
## '20 de cada mês'
teste = relativedelta(months=1)

print()
print(int(moth))

for x in range(int(moth)):
    x = data_inicio + relativedelta(months=1)
    data_inicio = x
    print(f'{x.strftime("%d/%m/%Y")} R$ {valor_parcela:.2f}')

print()
print(
    f'Você pegou R$ {emprestimo:,.2f} para pagar '
    f'em 5 anos '
    f'({int(moth)} meses) em parcelas de '
    f'R$ {format_valor_parcela}.'
)
print()


# print(data_inicio)
# print(delta)
# print(f'R$ {valor_parcela:.2f}')