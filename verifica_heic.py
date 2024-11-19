import os

def listar_arquivos_heic(diretorio_inicial, arquivo_saida):
    heic_paths = []

    # Percorre diretórios e subdiretórios
    for root, _, files in os.walk(diretorio_inicial):
        for file in files:
            # Verifica se o arquivo é .HEIC (case-insensitive)
            if file.lower().endswith(".heic"):
                full_path = os.path.join(root, file)
                heic_paths.append(full_path)
    
    # Ordena os caminhos em ordem alfabética
    heic_paths.sort()

    # Escreve os caminhos no arquivo de saída
    with open(arquivo_saida, 'w') as f:
        for path in heic_paths:
            f.write(f"{path}\n")

    print(f"Lista de arquivos .HEIC salva em: {arquivo_saida}")

# Exemplo de uso
diretorio_inicial = "D:\\Pictures"  # Altere para o caminho desejado
arquivo_saida = "lista_arquivos_heic_d_imagens.txt"  # Nome do arquivo de saída
listar_arquivos_heic(diretorio_inicial, arquivo_saida)