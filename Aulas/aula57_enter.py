class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None
    
    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()



with MyOpen('aula57.txt', 'w') as arquivo:
    arquivo.write('Exemplo 01\n')
    arquivo.write('Exemplo 02\n')
    arquivo.write('Exemplo 03\n')
    print('WITH', arquivo)