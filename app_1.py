import os
import json
import shutil
import logging
from utils import buscar_arquivos, extrai_hash, configurar_logs

# Carregando configurações
with open("config.json", encoding="utf-8") as config_file:
    config = json.load(config_file)

configurar_logs(config["log_file"])

arquivos_unicos = {}
contador = 0

arquivos = buscar_arquivos(config["diretorio_a_examinar_1"], config["extensoes"])

for arquivo in arquivos:
    contador += 1
    hash = extrai_hash(arquivo)
    if hash is None:
        continue

    if hash in arquivos_unicos:
        destino = f"{config['diretorio_destino_repetidas']}/{contador}_{os.path.basename(arquivo)}"
        try:
            shutil.move(arquivo, destino)
        except Exception as e:
            logging.error(f"Erro ao mover arquivo {arquivo} para {destino}: {str(e)}")
    else:
        arquivos_unicos[hash] = arquivo

with open(config["arquivo_json"], "w") as file:
    json.dump(arquivos_unicos, file, indent=4)