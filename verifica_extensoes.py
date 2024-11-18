import os

def listar_extensoes(diretorio):
    """
    Lista as extensões de todos os arquivos em um diretório e seus subdiretórios.

    Args:
        diretorio: O caminho do diretório a ser percorrido.
    """

    extensoes = {}
    for raiz, diretorios, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            _, extensao = os.path.splitext(arquivo)
            extensoes[extensao] = extensoes.get(extensao, 0) + 1

    # Imprimir o resultado
    for extensao, contagem in extensoes.items():
        print(f"Extensão: {extensao}, Contagem: {contagem}")

# Exemplo de uso
diretorio = "E:\\fotos (até 2016 - antigo D)"  # Substitua pelo caminho desejado
listar_extensoes(diretorio)