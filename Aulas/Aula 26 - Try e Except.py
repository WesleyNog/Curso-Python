try:
    a = 1/0
except NameError as erro:
    print('Erro do desenvolvedor!')
except (IndexError, KeyError) as erro:
    print('Erro no indice ou chave')
except Exception as erro:
    print('Erro inesperado!')
else:
    print('Seu código foi executado com sucesso')
finally:
    print("Finalmente.")

print('Bora continuar!')
