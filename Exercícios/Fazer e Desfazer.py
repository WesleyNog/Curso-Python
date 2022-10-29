
def refazer(tarefa, ta_exc):
    if not ta_exc:
        print('Nada para refazer!')
        return

    last_exc = ta_exc.pop()
    tarefa.append(last_exc)


tarefa = []
ta_exc = []

while True:
    acao = input('Digite uma TAREFA ou [R]-Refazer [D]-Desfazer [M]-Mostrar [ENTER]-Sair: ').upper()
    if acao == 'M':
        mostrar_tarefa(tarefa)
        continue
    elif acao == 'D':
        desfazer(tarefa, ta_exc)
        continue
    elif acao == 'R':
        refazer(tarefa, ta_exc)
        continue

    add(acao, tarefa)
