import json

# Caminhos dos arquivos JSON
arquivo1 = 'fotos_do_e_ate_2016.json'
arquivo2 = 'imagens_unicos.json'

# Carregar os arquivos JSON
with open(arquivo1, 'r', encoding='utf-8') as f1:
    dados1 = json.load(f1)

with open(arquivo2, 'r', encoding='utf-8') as f2:
    dados2 = json.load(f2)

# Juntar os dois dicionários
dados_combinados = {**dados1, **dados2}

# Salvar o dicionário combinado em um novo arquivo JSON (opcional)
with open('dados_combinados.json', 'w', encoding='utf-8') as f:
    json.dump(dados_combinados, f, ensure_ascii=False, indent=4)