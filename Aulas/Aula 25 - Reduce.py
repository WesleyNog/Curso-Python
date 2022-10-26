from Dados import pessoas, produtos, lista
from functools import reduce

media_idade = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(media_idade / len(pessoas))
